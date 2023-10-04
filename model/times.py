class Time:

    def __init__(self, treinador, categoria, turma, jogador):
        self.treinador = treinador
        self.categoria = categoria
        self.turma = turma
        self.jogador = jogador

    def get_treinador(self):
        return self.treinador
    
    def set_treinador(self, novo_treinador):
        self.treinador = novo_treinador

    def get_categoria(self):
        return self.categoria
    
    def set_categoria(self, nova_categoria):
        self.categoria = nova_categoria

    def get_turma(self):
        return self.turma

    def set_turma(self, nova_turma):
        self.turma = nova_turma

    def get_jogador(self):
        return self.jogador

    def set_jogador(self, novo_jogador):
        self.jogador = novo_jogador

    def to_string(self):
        return f"Treinador: {self.treinador} :: Categoria: {self.categoria}"