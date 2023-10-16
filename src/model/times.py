from model.turmas import Turma

class Time:
    def __init__(self, id_time:int=None, nome:str=None, treinador:str=None,categoria:str=None, turma:Turma=None):
        self.id_time = id_time
        self.nome = nome
        self.treinador = treinador
        self.categoria = categoria
        self.turma = turma

    def get_id_time(self) -> int:
        return self.id_time
    
    def set_id_time(self, novo_id_time:int):
        self.id_time = novo_id_time

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, novo_nome:str):
        self.nome = novo_nome

    def get_treinador(self) -> str:
        return self.treinador
    
    def set_treinador(self, novo_treinador:str):
        self.treinador = novo_treinador

    def get_categoria(self) -> str:
        return self.categoria
    
    def set_categoria(self, nova_categoria:str):
        self.categoria = nova_categoria

    def get_turma(self) -> Turma:
        return self.turma
    
    def set_turma(self, nova_turma:Turma):
        self.turma = nova_turma

    def to_string(self) -> str:
        return f"{self.get_nome()} | {self.get_treinador()} | {self.get_categoria()} | {self.get_turma().get_ano()}"
    