from conexion.oracle_queries import OracleQueries

def executar_script(script: str, insercao=False) -> None:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for comando in script:
        if comando:
            try:
                if insercao:
                    oracle.write(comando)
                else:
                    oracle.executeDDL(comando)
            except Exception as erro:
                print(f"[!] Ocorreu o seguinte erro: {erro}")

if __name__ == "__main__":
    with open("../sql/criacao_tabelas.sql") as f:
        primeiroScript = f.read().split(";")

    with open("../sql/insercao_registros.sql") as f:
        segundoScript = f.read().split(";")

    with open("../sql/insercao_registros_relacionados.sql") as f:
        terceiroScript = f.read().split("--")

    executar_script(primeiroScript)
    executar_script(segundoScript, insercao=True)
    executar_script(terceiroScript, insercao=True)