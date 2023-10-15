from conexion.oracle_queries import OracleQueries
from model.escolas import Escola
from typing import Union

import json

class ControllerEscola:
    def __init__(self):
        pass

    def inserir_registro(self) -> Union[Escola, None]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
       
        cnpj = input("Insira o CNPJ (somente os numeros): ").strip()

        if not self.verificar_registro(cnpj):
            nome = input("Nome da escola: ").strip()
            nivel_ensino = input("Nível de ensino da escola (fundamental/medio/infantil): ").strip()
            endereco = input("Endereço da escola: ").strip()
            telefone = input("Número de telefone da escola (apenas numeros): ").strip()
            oracle.write(f"INSERT INTO ESCOLAS VALUES ('{cnpj}', '{nome}', '{nivel_ensino}', '{endereco}', '{telefone}')")

            registro_escola = oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj}'")
            registro_escola = json.loads(registro_escola)[0]

            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            print("[+]", escola.to_string())
            return escola
        else:
            print("[!] Registro já existente no sistema.")
            return None
       
    def atualizar_registro(self) -> Union[Escola, None]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cnpj = input("Insira o CNPJ (somente os numeros): ").strip()

        if self.verificar_registro(cnpj):
            print("Qual dado deseja alterar?\n1 - Nome\n2 - Telefone\n")
            tipo_dado = int(input("Tipo de dado: "))

            if not tipo_dado in [1, 2]:
                print("[!] Opção inválida. Tente novamente.")
                return None
           
            if tipo_dado == 1:
                novo_nome = input("Novo nome da escola: ").strip()
                oracle.write(f"UPDATE ESCOLAS SET NOME = '{novo_nome}' WHERE CNPJ = '{cnpj}'")

            elif tipo_dado == 2:
                novo_telefone = input("Novo telefone da escola: ").strip()
                oracle.write(f"UPDATE ESCOLAS SET TELEFONE = '{novo_telefone}' WHERE CNPJ = '{cnpj}'")

            registro_escola = oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj}'")
            registro_escola = json.loads(registro_escola)[0]

            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            print("[+]", escola.to_string())
            return escola
        else:
            print("[!] Registro não existente no sistema.")
            return None

    def deletar_registro(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cnpj = input("Insira o CNPJ (somente os numeros): ").strip()

        if self.verificar_registro(cnpj):
            pass
        else:
            print("[!] Registro não existente no sistema.")
            return None

    def verificar_registro(self, cnpj: str) -> bool:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado_consulta = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = {cnpj}"))
        return bool(resultado_consulta)