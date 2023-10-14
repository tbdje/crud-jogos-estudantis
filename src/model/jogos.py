from datetime import datetime
from escolas import Escola

class Jogo:
    def __init__(self, datahora: datetime, escola: Escola):
        self.datahora = datahora
        self.escola = escola

    def get_datahora(self) -> datetime:
        return self.datahora
    
    def set_datahora(self, nova_datahora: datetime):
        self.datahora = nova_datahora

    def get_escola(self) -> Escola:
        return self.escola
    
    def set_escola(self, nova_escola: Escola):
        self.escola = nova_escola

    def __str__(self) -> str:
        return f"{self.get_datahora()} | {self.get_escola().get_nome()}"