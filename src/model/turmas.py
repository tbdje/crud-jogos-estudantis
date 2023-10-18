from model.escolas import Escola

class Turma:
    def __init__(self, id_turma:int=None, ano:str=None, quantidade_alunos:int=None, cnpj:Escola=None):
        self.id_turma = id_turma
        self.ano = ano
        self.quantidade_alunos = quantidade_alunos
        self.cnpj = cnpj

    def get_id_turma(self) -> int:
        return self.id_turma
    
    def set_id_turma(self, novo_id_turma):
        self.id_turma = novo_id_turma

    def get_ano(self) -> str:
        return self.ano
    
    def set_ano(self, novo_ano: str):
        self.ano = novo_ano

    def get_quantidade_alunos(self) -> int:
        return self.quantidade_alunos
    
    def set_quantidade_alunos(self, nova_quantidade: int):
        self.quantidade_alunos = nova_quantidade

    def get_cnpj(self) -> Escola:
        return self.cnpj
    
    def set_cnpj(self, novo_cnpj: Escola):
        self.cnpj = novo_cnpj

    def to_string(self):
        return f"{self.get_id_turma()} | {self.get_ano()} | {self.get_quantidade_alunos()} | {self.get_cnpj().get_nome()}"