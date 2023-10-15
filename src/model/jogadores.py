from model.times import Time

class Jogador:
    def __init__(self, cpf:str=None, nome:str=None, idade:int=None, posicao:str=None, numero_camisa:int=None, time:Time=None):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.numero_camisa = numero_camisa
        self.time = time

    def get_cpf(self) -> str:
        return self.cpf
    
    def set_cpf(self, novo_cpf:str):
        self.cpf = novo_cpf

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, novo_nome:str):
        self.nome = novo_nome

    def get_idade(self) -> int:
        return self.idade
    
    def set_idade(self, nova_idade:int):
        self.idade = nova_idade

    def get_posicao(self) -> str:
        return self.posicao
    
    def set_posicao(self, nova_posicao:str):
        self.posicao = nova_posicao

    def get_numero_camisa(self) -> int:
        return self.numero_camisa
    
    def set_numero_camisa(self, novo_numero:int):
        self.numero_camisa = novo_numero

    def get_time(self) -> Time:
        return self.time
    
    def set_time(self, novo_time:Time):
        self.time = novo_time

    def to_string(self) -> str:
        return f"{self.get_cpf()} | {self.get_nome()} | {self.get_idade()} | {self.get_posicao()} | {self.get_numero_camisa()} | {self.get_time().get_nome()}"