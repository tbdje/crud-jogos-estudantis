class Jogador:

    def __init__(self, nome, idade, posicao, numero_camisa, time):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.numero_camisa = numero_camisa
        self.time = time

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade

    def set_idade(self, novo_idade):
        self.idade = novo_idade

    def get_posicao(self):
        return self.posicao

    def set_posicao(self, novo_posicao):
        self.posicao = novo_posicao

    def get_numero_camisa(self):
        return self.numero_camisa

    def set_numero_camisa(self, novo_numero_camisa):
        self.numero_camisa = novo_numero_camisa

    def get_time(self):
        return self.time

    def set_time(self, novo_time):
        self.time = novo_time

    def to_string(self):
        return f"Nome: {self.nome} :: Idade: {self.idade} :: Posição: {self.posicao} :: Número: {self.numero_camisa}"