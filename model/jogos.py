from escolas import Escola
from times import Time

from datetime import datetime

class Jogo:
    def __init__(self, datahora: datetime, escola: Escola, time: Time):
        self.datahora = datahora
        self.escola = escola
        self.time = time

    def get_datahora(self) -> datetime:
        return self.datahora
    
    def set_datahora(self, nova_datahora: datetime):
        self.datahora = nova_datahora

    def get_escola(self) -> Escola:
        return self.escola
    
    def set_escola(self, nova_escola: Escola):
        self.escola = nova_escola

    def get_time(self) -> Time:
        return self.time
    
    def set_time(self, novo_time: Time):
        self.time = novo_time

    def __str__(self) -> str:
        return f"{self.get_datahora()} | {self.get_escola().get_nome()} | {self.get_time().get_nome()}"
    