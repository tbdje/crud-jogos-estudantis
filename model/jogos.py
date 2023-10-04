class Jogo:

    def __init__(self, data, horario, escola, time):
        self.data = data
        self.horario = horario
        self.escola = escola
        self.time = time

    def get_data(self):
        return self.data

    def set_data(self, nova_data):
        self.data = nova_data

    def get_horario(self):
        return self.horario
    
    def set_horario(self, novo_horario):
        self.horario = novo_horario

    def get_escola(self):
        return self.escola

    def set_escola(self, nova_escola):
        self.escola = nova_escola

    def get_time(self):
        return self.time

    def set_time(self, novo_time):
        self.time = novo_time

    def to_string(self):
        return f"Data: {self.data} :: Horário: {self.horario}"