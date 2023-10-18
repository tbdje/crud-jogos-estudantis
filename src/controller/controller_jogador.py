from controller.controller_time import ControllerTime
from conexion.oracle_queries import OracleQueries
from model.times import Time
from model.jogos import Jogo
from model.escolas import Escola
from model.turmas import Turma
from model.jogadores import Jogador

from typing import Union

import json

class ControllerJogador:
    def __init__(self):
        self.controller_time = ControllerTime()

    def inserir_registro(self) -> Union[Time, None]:
        self.listar_times()
        id_time_jogador = int(input("Insira o ID do time para o jogador: "))
        time = self.validar_time(id_time_jogador)

        if time is None:
            return None
       
        cpf_jogador = input("Insira o CPF do jogador (somente números): ").strip()
        nome_jogador = input("Nome do jogador: ").strip()
        idade_jogador = int(input("Idade do jogador: "))
        posicao_campo = input("Posição do jogador: ").strip()
        numero_camisa = int(input("Número da camisa do jogador: "))

        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(f"INSERT INTO JOGADORES VALUES ('{cpf_jogador}', '{nome_jogador}', '{idade_jogador}', '{posicao_campo}', '{numero_camisa}', '{id_time_jogador}')")

        registro_jogador = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGADORES WHERE CPF = '{cpf_jogador}'"))[0]
        novo_jogador = Jogador(registro_jogador["cpf"], registro_jogador["nome"], registro_jogador["idade"], registro_jogador["posicao"], registro_jogador["numero_camisa"], time)

        print("[+]", novo_jogador.to_string())
        return novo_jogador

    def atualizar_registro(self) -> Union[Jogador, None]:
        cpf_jogador = input("Insira o CPF do jogador para alterar: ").strip()

        if self.verificar_registro(cpf_jogador):
            nova_posicao = input("Insira a nova posicao do jogador: ").strip()
            novo_numero = input("Insira o novo numero: ").strip()

            oracle = OracleQueries(can_write=True)
            oracle.connect()

            oracle.write(f"UPDATE JOGADORES SET POSICAO = '{nova_posicao}', NUMERO_CAMISA = '{novo_numero}' WHERE CPF = '{cpf_jogador}'")

            registro_jogador = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGADORES WHERE CPF = '{cpf_jogador}'"))[0]
            time = self.validar_time(registro_jogador["id_time"])
            novo_jogador = Jogador(registro_jogador["cpf"], registro_jogador["nome"], registro_jogador["idade"], registro_jogador["posicao"], registro_jogador["numero_camisa"], time)

            print("[^+]", novo_jogador.to_string())

            return novo_jogador
        else:
            print("[!] Esse jogador não existe no sistema.")
            return None

    def deletar_registro(self) -> Union[Jogador, None]:
        cpf_jogador = input("Insira o CPF do jogador que deseja deletar: ").strip()

        if self.verificar_registro(cpf_jogador):
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            registro_jogador = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGADORES WHERE CPF = {cpf_jogador}"))[0]

            oracle.write(f"DELETE FROM JOGADORES WHERE CPF = {cpf_jogador}")

            time = self.validar_time(registro_jogador["id_time"])
            jogador = Jogador(registro_jogador["cpf"], registro_jogador["nome"], registro_jogador["idade"], registro_jogador["posicao"], registro_jogador["numero_camisa"], time)

            print("[-]", jogador.to_string())
            return jogador
        else:
            print("[!] Jogador não existente no sistema.")
            return None

    def listar_times(self):
        oracle = OracleQueries()
        oracle.connect()
        times = oracle.sqlToDataFrame("SELECT ID_TIME, NOME, TREINADOR FROM TIMES")
        print(times)

    def listar_jogadores(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame("SELECT * FROM JOGADORES"))

    def validar_time(self, id_time:str) -> Union[Time, None]:
        if self.controller_time.verificar_registro(id_time):
            oracle = OracleQueries()
            oracle.connect()
            registro_time = json.loads(oracle.sqlToJson(f"SELECT * FROM TIMES WHERE ID_TIME = '{id_time}'"))[0]
            registro_jogo = json.loads(oracle.sqlToJson(f"SELECT * FROM JOGOS WHERE ID_JOGO = '{registro_time['id_jogo']}'"))[0]
            registro_turma = json.loads(oracle.sqlToJson(f"SELECT * FROM TURMAS WHERE ID_TURMA = '{registro_time['id_turma']}'"))[0]
            registro_escola = json.loads(oracle.sqlToJson(f"SELECT * FROM ESCOLAS WHERE CNPJ = '{registro_jogo['cnpj']}'"))[0]
            escola = Escola(registro_escola["cnpj"], registro_escola["nome"], registro_escola["nivel_ensino"], registro_escola["endereco"], registro_escola["telefone"])
            turma = Turma(registro_turma["id_turma"], registro_turma["ano"], registro_turma["quantidade_alunos"], escola)
            jogo = Jogo(registro_jogo["id_jogo"], registro_jogo["data_hora"], escola)
            time = Time(registro_time["id_time"], registro_time["nome"], registro_time["treinador"], registro_time["categoria"], turma, jogo)
            return time
        else:
            return None

    def verificar_registro(self, cpf_jogador:str) -> bool:
        oracle = OracleQueries()
        oracle.connect()
        consulta_jogador = json.loads(oracle.sqlToJson(f"SELECT CPF FROM JOGADORES WHERE CPF = {cpf_jogador}"))
        return bool(consulta_jogador)