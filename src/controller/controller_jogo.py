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

        mapeamento_jogo = dict(id_jogo=tipo_dado_codigo, datahora=datahora, escola=escola.get_cnpj())

        cursor.execute("""
        BEGIN
            :ID_JOGO := JOGOS_ID_SEQ.NEXTVAL;
            INSERT  INTO JOGOS VALUES (:ID_JOGO, :DATA_HORA, :CNPJ)
        END;
        """, mapeamento_jogo)

        id_jogo = tipo_dado_codigo.getvalue()
        oracle.conn.commit()

    def atualizar_registro(self):
        pass

    def deletar_registro(self):
        pass

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

    def listar_escolas(self) -> None:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado = oracle.sqlToDataFrame("SELECT CNPJ, NOME, ENDERECO FROM ESCOLAS ORDER BY NOME")
        print(resultado)