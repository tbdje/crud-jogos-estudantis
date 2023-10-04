class Escola:

    def __init__(self, nome, nivel_ensino, endereco, telefone):
        self.nome = nome
        self.nivel_ensino = nivel_ensino
        self.endereco = endereco
        self.telefone = telefone

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_nivel_ensino(self):
        return self.nivel_ensino

    def set_nivel_ensino(self, novo_nivel_ensino):
        self.nivel_ensino = novo_nivel_ensino

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def to_string(self):
        return f"Nome: {self.nome} :: Nível de Ensino: {self.nivel_ensino} :: Endereço: {self.endereco} :: Telefone: {self.telefone}"