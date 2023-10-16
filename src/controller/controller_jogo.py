from conexion.oracle_queries import OracleQueries
from controller.controller_escola import ControllerEscola
from model.jogos import Jogo
from model.escolas import Escola

from typing import Union
from datetime import datetime

import json

class ControllerJogo:
    def __init__(self):
        self.controller_escola = ControllerEscola()

    def inserir_registro(self):
        self.listar_escolas()
        cnpj_escola = input("Digite o CNPJ da escola desejada: ").strip()
        escola = self.validar_escola(cnpj_escola)

        if escola is None:
            return None
       
        data_jogo = input("Insira a data que ocorrerá o jogo (dia/mes/ano): ").strip()
        hora_jogo = input("Insira a hora em que o jogo acontecerá (hora:minuto): ").strip()

        dia, mes, ano = list(map(int, data_jogo.split("/")))
        hora, minuto = list(map(int, hora_jogo.split(":")))
       
        datahora = datetime(ano, mes, dia, hora, minuto).strftime("%Y-%m-%d %H:%M")

        oracle = OracleQueries(can_write=True)
        cursor = oracle.connect()
        tipo_dado_codigo = cursor.var(int)

        mapeamento_jogo = dict(id_jogo=tipo_dado_codigo, datahora=datahora, cnpj=escola.get_cnpj())

        cursor.execute(f"""
        BEGIN
            :id_jogo := JOGOS_ID_SEQ.NEXTVAL;
            INSERT INTO JOGOS VALUES(:id_jogo, TO_TIMESTAMP(:datahora, 'YYYY-MM-DD HH24:MI'), :cnpj);
        END;
        """, mapeamento_jogo)

        id_do_jogo = tipo_dado_codigo.getvalue()
        oracle.conn.commit()

        registro_jogo = json.loads(oracle.sqlToJson(f"SELECT DATA_HORA FROM JOGOS WHERE ID_JOGO = {id_do_jogo}"))[0]
        jogo = Jogo(id_do_jogo, registro_jogo["data_hora"], escola)

        print(jogo.to_string())
        return jogo

    def atualizar_registro(self) -> Union[Jogo, None]:
        self.listar_jogos()
        id_jogo = int(input("Insira o ID do jogo que deseja alterar: ").strip())

        if self.verificar_registro(id_jogo):            
            data_jogo = input("Insira a nova data do jogo (dia/mes/ano): ").strip()
            hora_jogo = input("Insira o horário: (hora:minuto): ").strip()

            dia, mes, ano = list(map(int, data_jogo.split("/")))
            hora, minuto = list(map(int, hora_jogo.split(":")))

            datahora = datetime(ano, mes, dia, hora, minuto).strftime("%Y-%m-%d %H:%M")

            oracle = OracleQueries(can_write=True)
            oracle.connect()

            oracle.write(f"UPDATE JOGOS SET DATA_HORA = TO_TIMESTAMP('{datahora}', 'YYYY-MM-DD HH24:MI') WHERE ID_JOGO = {id_jogo}")

        else:
            print("[!] Esse jogo não existe no sistema.")
            return None
       

    def deletar_registro(self) -> Union[Jogo, None]:
        id_jogo = int(input("Insira o ID do jogo que deseja deletar: "))

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        if self.verificar_registro(id_jogo):
            registro_jogo = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = {id_jogo}"))[0]
            registro_escola = self.validar_escola(registro_jogo["cnpj"])

            escolha = input(f"Deseja excluir o jogo de ID {id_jogo}? [sim/nao]: ").lower()[0]

            if escolha == "s":
                print("[!] Caso existam times cadastrados no jogo, os mesmos serão retirados, mas não deletados.")
                escolha = input(f"Confirma a exclusão do jogo de ID {id_jogo}? [sim/nao]: ").lower()[0]

                if escolha == "s":
                    if bool(json.loads(oracle.sqlToJson(f"SELECT ID_TIME FROM TIMES WHERE ID_JOGO = '{id_jogo}'"))):
                        oracle.write(f"UPDATE TIMES SET ID_JOGO = NULL WHERE ID_JOGO = '{id_jogo}'")
                        print("[-] Times retirados do jogo.")

                    oracle.write(f"DELETE FROM JOGOS WHERE ID_JOGO = '{id_jogo}'")

                    jogo = Jogo(id_jogo, registro_jogo["data_hora"], registro_escola)

                    print("[-] Jogo removido.")
                    print(jogo.to_string())
                    return jogo
        else:
            print("[!] Jogo não cadastrado no sistema.")
            return None

    def verificar_registro(self, id_jogo:int) -> bool:
        oracle = OracleQueries()
        oracle.connect()
        resultado = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = {id_jogo}"))[0]
        return bool(resultado)

    def validar_escola(self, cnpj: str) -> Union[Escola, None]:
        oracle = OracleQueries()
        oracle.connect()
        escola_existe = self.controller_escola.verificar_registro(cnpj)

        if escola_existe:
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj}'"))[0]
            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            return escola
        else:
            print("[!] Escola não cadastrada no sistema.")
            return None
       
    def listar_jogos(self) -> None:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado = oracle.sqlToDataFrame("SELECT J.ID_JOGO, J.DATA_HORA, E.NOME AS NOME_ESCOLA FROM JOGOS J INNER JOIN ESCOLAS E ON J.CNPJ = E.CNPJ")
        print(resultado)

    def listar_escolas(self) -> None:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado = oracle.sqlToDataFrame("SELECT CNPJ, NOME, ENDERECO FROM ESCOLAS ORDER BY NOME")
        print(resultado)