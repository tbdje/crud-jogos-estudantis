from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_jogadores.sql") as rel_jog_cont:
            self.rel_jogd = rel_jog_cont.read()

        with open("sql/relatorio_escolas.sql") as rel_esc_cont:
            self.rel_esc = rel_esc_cont.read()

        with open("sql/relatorio_jogos.sql") as rel_jog_cont:
            self.rel_jog = rel_jog_cont.read()

        with open("sql/relatorio_time_e_jogadores.sql") as rel_tj_cont:
            self.rel_tj = rel_tj_cont.read()

        with open("sql/relatorio_numero_jogos.sql") as rel_nj_cont:
            self.rel_nj = rel_nj_cont.read()

        with open("sql/relatorio_times.sql") as rel_tim_cont:
            self.rel_tim = rel_tim_cont.read()

        with open("sql/relatorio_turmas.sql") as rel_tur_cont:
            self.rel_tur = rel_tur_cont.read()

    def get_relatorio_jogadores(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_jogd))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_escolas(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_esc))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_jogos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_jog))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_times_jogadores(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_tj))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_numero_jogos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_nj))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_times(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_tim))
        input("[Enter] - Sair do Relatório Atual")

    def get_relatorio_turmas(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.rel_tur))
        input("[Enter] - Sair do Relatório Atual")