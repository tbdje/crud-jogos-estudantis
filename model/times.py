from turmas import Turma
from jogadores import Jogador

class Time:
    def __init__(self, nome: str, treinador: str, categoria: str, turma: Turma, jogador: Jogador):
        self.nome = nome
        self.treinador = treinador
        self.categoria = categoria
        self.turma = turma
        self.jogador = jogador

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, novo_nome: str):
        self.nome = novo_nome

    def get_treinador(self) -> str:
        return self.treinador
    
    def set_treinador(self, novo_treinador: str):
        self.treinador = novo_treinador

    def get_categoria(self) -> str:
        return self.categoria
    
    def set_categoria(self, nova_categoria: str):
        self.categoria = nova_categoria

    def get_turma(self) -> Turma:
        return self.turma
    
    def set_turma(self, nova_turma: Turma):
        self.turma = nova_turma

    def get_jogador(self) -> Jogador:
        return self.jogador
    
    def set_jogador(self, novo_jogador: Jogador):
        self.jogador = novo_jogador

    def __str__(self) -> str:
        return f"{self.get_nome()} | {self.get_treinador()} | {self.get_categoria()} | {self.get_turma().get_ano()} | {self.get_jogador().get_nome()}"
    