from datetime import datetime
from model.escolas import Escola

class Jogo:
    def __init__(self, id_jogo:int=None, datahora:datetime=None, escola:Escola=None):
        self.id_jogo = id_jogo
        self.datahora = datahora
        self.escola = escola

    def get_id_jogo(self) -> int:
        return self.id_jogo
    
    def set_id_jogo(self, novo_id_jogo:int):
        self.id_jogo = novo_id_jogo

    def get_datahora(self) -> datetime:
        return self.datahora
    
    def set_datahora(self, nova_datahora:datetime):
        self.datahora = nova_datahora

    def get_escola(self) -> Escola:
        return self.escola
    
    def set_escola(self, nova_escola:Escola):
        self.escola = nova_escola

    def __str__(self) -> str:
        return f"{self.get_datahora()} | {self.get_escola().get_nome()}"
    