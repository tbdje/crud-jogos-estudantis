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
            except Exception as e:
                print(f"[!] Ocorreu o seguinte erro: {e}")

if __name__ == "__main__":
    with open("../sql/criacao_tabelas.sql") as f:
        primeiroScript = f.read().split(";")

    with open("../sql/insercao_registros.sql") as f:
        segundoScript = f.read().split(";")

    with open("../sql/insercao_registros_relacionados.sql") as f:
        terceiroScript = f.read().split("--")

    executar_script(primeiroScript)
    print("[+] Tabelas criadas.")

    executar_script(segundoScript, insercao=True)
    print("[+] Registros inseridos.")

    executar_script(terceiroScript, insercao=True)
    print("[+] Registro relacionados inseridos.")