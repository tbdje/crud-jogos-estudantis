from escolas import Escola

class Turma:
    def __init__(self, ano: str, quantidade_alunos: int, escola: Escola):
        self.ano = ano
        self.quantidade_alunos = quantidade_alunos
        self.escola = escola

    def get_ano(self) -> str:
        return self.ano
    
    def set_ano(self, novo_ano: str):
        self.ano = novo_ano

    def get_quantidade_alunos(self) -> int:
        return self.quantidade_alunos
    
    def set_quantidade_alunos(self, nova_quantidade: int):
        self.quantidade_alunos = nova_quantidade

    def get_escola(self) -> Escola:
        return self.escola
    
    def set_escola(self, nova_escola: Escola):
        self.escola = nova_escola

    def __str__(self):
        return f"{self.get_ano()} | {self.get_quantidade_alunos()} | {self.get_escola().get_nome()}"