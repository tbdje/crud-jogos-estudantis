from model.turmas import Turma
from model.escolas import Escola
from controller.controller_escola import ControllerEscola
from conexion.oracle_queries import OracleQueries
from typing import Union

import json

class ControllerTurma:
    def __init__(self):
        self.controller_escola = ControllerEscola()

    def inserir_registro(self) -> Union[Turma, None]:
        self.listar_escolas()
        cnpj_escola = input("Insira o CNPJ da escola desejada: ")
        registro_escola = self.validar_escola(cnpj_escola)

        if registro_escola is None:
            return None

        oracle = OracleQueries(can_write=True)
        cursor = oracle.connect()

        ano_turma = input("Insira o ano da turma (ano+letra): ").strip()
        quantidade_alunos = input("Insira a quantidade de alunos: ").strip()
        tipo_dado_id = cursor.var(int)

        mapeamento_turma = dict(id_turma=tipo_dado_id, ano=ano_turma, quantidade_alunos=quantidade_alunos, cnpj=registro_escola.get_cnpj())

        cursor.execute("""
        BEGIN
            :id_turma := TURMAS_ID_SEQ.NEXTVAL;
            INSERT INTO TURMAS VALUES (:id_turma, :ano, :quantidade_alunos, :cnpj);
        END;
        """, mapeamento_turma)

        id_turma = tipo_dado_id.getvalue()
        oracle.conn.commit()

        registro_turma = json.loads(oracle.sqlToJson(F"SELECT ID_TURMA, ANO, QUANTIDADE_ALUNOS FROM TURMAS WHERE ID_TURMA = '{id_turma}'"))[0]
        turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], registro_escola)
        print("[+]", turma.to_string())
        return turma
    
    def atualizar_registro(self) -> Union[Turma, None]:
        id_turma = int(input("ID da turma que deseja alterar: "))

        if self.verificar_registro(id_turma):
            nova_quantidade_alunos = int(input("Insira a nova quantidade de alunos: "))
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            oracle.write(f"UPDATE TURMAS SET QUANTIDADE_ALUNOS = '{nova_quantidade_alunos}' WHERE ID_TURMA = '{id_turma}'")

            registro_turma = json.loads(oracle.sqlToJson(f"SELECT ID_TURMA, ANO, QUANTIDADE_ALUNOS, CNPJ FROM TURMAS WHERE ID_TURMA = '{id_turma}'"))[0]
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = {registro_turma['cnpj']}"))[0]

            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)

            print("[^+]", turma.to_string())
            return turma
        else:
            print("[!] A turma não existe no sistema.")
            return None

    def deletar_registro(self) -> Union[Turma, None]:
        id_turma = int(input("ID da turma que deseja deletar: "))

        if self.verificar_registro(id_turma):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            registro_turma = json.loads(oracle.sqlToJson(f"SELECT * FROM TURMAS WHERE ID_TURMA = '{id_turma}'"))[0]
            escolha = input("Confirma que deseja deletar a turma? [sim/nao]: ").lower()[0]

            if escolha == "s":
                escolha = input("Todos os jogadores e times da turma serão deletados. Confirma a exclusão? [sim/nao]: ").lower()[0]

                if escolha == "s":
                    id_time = bool(json.loads(oracle.sqlToJson(f"SELECT ID_TIME FROM TIMES WHERE ID_TURMA = '{id_turma}'")))
                    
                    if id_time:
                        id_time = id_time[0]["id_time"]
                        cpfs_jogadores = json.loads(oracle.sqlToJson(f"SELECT CPF FROM JOGADORES WHERE ID_TIME = '{id_time}'"))

                        if cpfs_jogadores:
                            for cpf in cpfs_jogadores:
                                oracle.write(f"DELETE FROM JOGADORES WHERE CPF = '{cpf['cpf']}'")
                            
                            print("[-] Jogadores removidos.")

                        oracle.write(f"DELETE FROM TIMES WHERE ID_TIME = '{id_time}'")
                        print("[-] Time removido.")

                    oracle.write(f"DELETE FROM TURMAS WHERE ID_TURMA = {id_turma}")

                    registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{registro_turma['cnpj']}'"))[0]
                    escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
                    turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)

                    print("[-]", turma.to_string())
                    return turma
        else:
            print("[!] Turma não existente no sistema.")
            return None

    def listar_escolas(self):
        oracle = OracleQueries()
        oracle.connect()
        resultado = oracle.sqlToDataFrame("SELECT CNPJ, NOME, NIVEL_ENSINO FROM ESCOLAS")
        print(resultado)

    def validar_escola(self, cnpj:str):
        if self.controller_escola.verificar_registro(cnpj):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = {cnpj}"))[0]
            return Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
        else:
            return None
    
    def verificar_registro(self, id_turma:int):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado = json.loads(oracle.sqlToJson(f"SELECT ID_TURMA FROM TURMAS WHERE ID_TURMA = {id_turma}"))
        return bool(resultado)