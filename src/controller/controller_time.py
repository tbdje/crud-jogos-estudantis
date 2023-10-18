from controller.controller_turma import ControllerTurma
from controller.controller_jogo import ControllerJogo
from conexion.oracle_queries import OracleQueries

from model.times import Time
from model.turmas import Turma
from model.escolas import Escola
from model.jogos import Jogo

from typing import Union

import json

class ControllerTime:
    def __init__(self):
        self.controller_turma = ControllerTurma()
        self.controller_jogo = ControllerJogo()

    def inserir_registro(self) -> Union[Time, None]:
        self.listar_turmas()
        id_turma = int(input("Insira o ID da turma para o time: "))
        turma = self.validar_turma(id_turma)
        if turma is None:
            return None
       
        self.listar_jogos()
        id_jogo = int(input("Insira o ID do jogo para o time: "))
        jogo = self.validar_jogo(id_jogo)
        if jogo is None:
            return None
       
        nome_time = input("Insira o nome para o time: ").strip()
        nome_treinador = input("Insira o nome do treinador: ").strip()
        categoria = input("Insira a categoria [masculino/feminino]: ").strip()

        oracle = OracleQueries(can_write=True)
        cursor = oracle.connect()

        tipo_id_time = cursor.var(int)

        mapeamento_time = dict(
            id_time=tipo_id_time,
            nome=nome_time,
            treinador=nome_treinador,
            categoria=categoria,
            id_turma=turma.get_id_turma(),
            id_jogo=jogo.get_id_jogo()
            )

        cursor.execute("""
        begin
            :id_time := TIMES_ID_SEQ.NEXTVAL;
            INSERT INTO TIMES VALUES(:id_time, :nome, :treinador, :categoria, :id_turma, :id_jogo);  
        end;
        """, mapeamento_time)

        id_time = tipo_id_time.getvalue()
        oracle.conn.commit()
        time = Time(id_time, nome_time, nome_treinador, categoria, turma, jogo)
        print("[+]", time.to_string())
        return time

    def atualizar_registro(self) -> Union[Time, None]:
        id_time = int(input("Insira o ID do time para alterar: "))

        if self.verificar_registro(id_time):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            nome_novo_treinador = input("Insira o nome do novo treinador: ").strip()
            oracle.write(f"UPDATE TIMES SET TREINADOR = '{nome_novo_treinador}' WHERE ID_TIME = '{id_time}'")
            registro_time = json.loads(oracle.sqlToJson(f"SELECT * FROM TIMES WHERE ID_TIME = '{id_time}'"))[0]
            registro_jogo = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = '{registro_time['id_jogo']}'"))[0]
            registro_turma = json.loads(oracle.sqlToJson(f"SELECT * FROM TURMAS WHERE ID_TURMA = '{registro_time['id_turma']}'"))[0]
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{registro_turma['cnpj']}'"))[0]

            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)
            jogo = Jogo(registro_jogo["id_jogo"], registro_jogo["data_hora"], escola)

            novo = Time(registro_time["id_time"], registro_time["nome"], registro_time["treinador"], registro_time["categoria"], turma, jogo)
       
            print("[^+]", novo.to_string())
            return novo
        else:
            print("[!] Time não existe.")
            return None

    def deletar_registro(self) -> Union[Time, None]:
        id_time = int(input("Insira o ID do time que deseja deletar: "))

        if self.verificar_registro(id_time):
            escolha = input("O time escolhido será deletado, bem como os jogadores nele. Tem certeza? [sim/nao]: ").lower()[0]
            if escolha == "s":
                escolha = input("Tem certeza? [sim/nao]: ").lower()[0]
                if escolha == "s":
                    oracle = OracleQueries(can_write=True)
                    oracle.connect()
                    registro_time = json.loads(oracle.sqlToJson(f"SELECT * FROM TIMES WHERE ID_TIME = '{id_time}'"))[0]

                    jogadores = json.loads(oracle.sqlToJson(f"SELECT CPF FROM JOGADORES WHERE ID_TIME = '{id_time}'"))

                    if jogadores:
                        for cpf in jogadores:
                            oracle.write(f"DELETE FROM JOGADORES WHERE CPF = '{cpf['cpf']}'")

                    registro_turma = json.loads(oracle.sqlToJson(f"SELECT * FROM TURMAS WHERE ID_TURMA = '{registro_time['id_turma']}'"))[0]
                    registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{registro_turma['cnpj']}'"))[0]

                    escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
                    registro_jogo = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = '{registro_time['id_jogo']}'"))[0]

                    turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)
                    jogo = Jogo(registro_jogo["id_jogo"], registro_jogo["data_hora"], escola)

                    time = Time(registro_time["id_time"], registro_time["nome"], registro_time["treinador"], registro_time["categoria"], turma, jogo)

                    oracle.write(f"DELETE FROM TIMES WHERE ID_TIME = '{id_time}'")

                    print("[-]", time.to_string())

                    return time

        else:
            print("[!] Esse time não existe.")
            return None

    def validar_turma(self, id_turma:int) -> Union[Turma, None]:
        if self.controller_turma.verificar_registro(id_turma):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            registro_turma = json.loads(oracle.sqlToJson(f"SELECT * FROM TURMAS WHERE ID_TURMA = '{id_turma}'"))[0]
            cnpj = registro_turma["cnpj"]
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj}'"))[0]
            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)
            return turma
        else:
            return None

    def validar_jogo(self, id_jogo:int):
        if self.controller_jogo.verificar_registro(id_jogo):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            registro_jogo = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = '{id_jogo}'"))[0]
            cnpj_escola = registro_jogo["cnpj"]
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj_escola}'"))[0]
            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            jogo = Jogo(registro_jogo["id_jogo"], registro_jogo["data_hora"], escola)
            return jogo
        else:
            return None

    def listar_turmas(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        consulta = oracle.sqlToDataFrame("SELECT ID_TURMA, ANO, QUANTIDADE_ALUNOS FROM TURMAS")
        print(consulta)

    def listar_jogos(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        consulta = oracle.sqlToDataFrame("SELECT * FROM JOGOS")
        print(consulta)

    def verificar_registro(self, id_time:int) -> bool:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado = json.loads(oracle.sqlToJson(f"SELECT ID_TIME FROM TIMES WHERE ID_TIME = {id_time}"))
        return bool(resultado)