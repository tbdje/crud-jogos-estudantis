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
            print("[^+]", escola.to_string())
            return escola
        else:
            print("[!] Registro não existente no sistema.")
            return None

    def deletar_registro(self) -> Union[Escola, None]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cnpj = input("Insira o CNPJ (somente os numeros): ").strip()

        if self.verificar_registro(cnpj):
            confirmacao = input("Essa escola e registros ligados a ela serão excluidos, quer continuar? [sim/nao]: ").lower()[0]

            if confirmacao == "s":
                confirmacao = input("Confirma que deseja a exclusão? [sim/nao]: ").lower()[0]

                if confirmacao == "s":
                    registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{cnpj}'"))[0]
                    time_id = ""
                    jogador_cpf = ""

                    jogo_id = json.loads(oracle.sqlToJson(f"SELECT ID_JOGO FROM JOGOS WHERE CNPJ = '{registro_escola['cnpj']}'"))
                    turma_id = json.loads(oracle.sqlToJson(f"SELECT ID_TURMA FROM TURMAS WHERE CNPJ = '{registro_escola['cnpj']}'"))
                    if turma_id:
                        time_id = json.loads(oracle.sqlToJson(f"SELECT ID_TIME FROM TIMES WHERE ID_TURMA = '{turma_id[0]['id_turma']}'"))
                        if time_id:
                            jogador_cpf = json.loads(oracle.sqlToJson(f"SELECT CPF FROM JOGADORES WHERE ID_TIME = '{time_id[0]['id_time']}'"))

                    if jogador_cpf:
                        jogador_cpf = jogador_cpf[0]
                        oracle.write(f"DELETE FROM JOGADORES WHERE CPF = '{jogador_cpf['cpf']}'")
                    
                    if jogo_id:
                        jogo_id = jogo_id[0]
                        oracle.write(f"DELETE FROM JOGOS WHERE ID_JOGO = '{jogo_id['id_jogo']}'")

                    if time_id:
                        time_id = time_id[0]
                        oracle.write(f"DELETE FROM TIMES WHERE ID_TIME = '{time_id['id_time']}'")
                    
                    if turma_id:
                        turma_id = turma_id[0]
                        oracle.write(f"DELETE FROM TURMAS WHERE ID_TURMA = '{turma_id['id_turma']}'")

                    oracle.write(f"DELETE FROM ESCOLAS WHERE CNPJ = '{cnpj}'")

                    escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
                    print("[-]", escola.to_string())
                    return escola
        else:
            print("[!] Registro não existente no sistema.")
            return None

    def verificar_registro(self, cnpj: str) -> bool:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        resultado_consulta = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = {cnpj}"))
        return bool(resultado_consulta)