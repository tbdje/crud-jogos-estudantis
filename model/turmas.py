class Turma:

    def __init__(self, ano, letra, quantidade_alunos, escola):
        self.ano = ano
        self.letra = letra
        self.quantidade_alunos = quantidade_alunos
        self.escola = escola

    def get_ano(self):
        return self.ano

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_letra(self):
        return self.letra

    def set_letra(self, nova_letra):
        self.letra = nova_letra

    def get_quantidade_alunos(self):
        return self.quantidade_alunos

    def set_quantidade_alunos(self, novo_quantidade_alunos):
        self.quantidade_alunos = novo_quantidade_alunos

    def get_escola(self):
        return self.escola

    def set_escola(self, nova_escola):
        self.escola = nova_escola

    def to_string(self):
        return f"Ano: {self.ano} :: Letra: {self.letra} :: Quantidade de alunos: {self.quantidade_alunos}"