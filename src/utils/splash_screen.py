from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:
    def __init__(self):
        self.consulta_qtd_escolas = config.CONSULTA_QUANTIDADE.format(tabela="escolas")
        self.consulta_qtd_jogadores = config.CONSULTA_QUANTIDADE.format(tabela="jogadores")
        self.consulta_qtd_turmas = config.CONSULTA_QUANTIDADE.format(tabela="turmas")
        self.consulta_qtd_jogos = config.CONSULTA_QUANTIDADE.format(tabela="jogos")
        self.consulta_qtd_times = config.CONSULTA_QUANTIDADE.format(tabela="times")

        self.created_by = "Felipe L. Nunes, Rafael Pereira,\n Ramiro Biazatti, Amanda de Moraes e Pedro Pimentel."
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_qtd_escolas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.consulta_qtd_escolas)["total_escolas"].values[0]
    
    def get_qtd_jogadores(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.consulta_qtd_jogadores)["total_jogadores"].values[0]

    def get_qtd_turmas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.consulta_qtd_turmas)["total_turmas"].values[0]
    
    def get_qtd_jogos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.consulta_qtd_jogos)["total_jogos"].values[0]
    
    def get_qtd_times(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.consulta_qtd_times)["total_times"].values[0]

    def get_updated_screen(self):
        return f"""
##########################################################
            ---= SISTEMA DE JOGOS ESTUDANTIS =---                     
##########################################################
          
 QUANTIDADE ENTIDADES NO SISTEMA:                            

    1. ESCOLAS: {str(self.get_qtd_escolas()).ljust(5)}
    2. JOGADORES: {str(self.get_qtd_jogadores()).ljust(5)}
    3. TURMAS: {str(self.get_qtd_turmas()).ljust(5)}
    4. JOGOS: {str(self.get_qtd_jogos()).ljust(5)}
    5. TIMES: {str(self.get_qtd_times()).ljust(5)}

 CRIADO POR:
 {self.created_by}

 PROFESSOR: {self.professor}

 DISCIPLINA: {self.disciplina}
             {self.semestre}
########################################################
        """