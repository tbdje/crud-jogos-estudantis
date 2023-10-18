from controller.controller_escola import ControllerEscola
from controller.controller_jogador import ControllerJogador
from controller.controller_jogo import ControllerJogo
from controller.controller_time import ControllerTime
from controller.controller_turma import ControllerTurma

from utils import config
from utils.splash_screen import SplashScreen

from reports.relatorios import Relatorio

splash_screen = SplashScreen()
relatorio = Relatorio()

controller_escola = ControllerEscola()
controller_jogador = ControllerJogador()
controller_jogo = ControllerJogo()
controller_time = ControllerTime()
controller_turma = ControllerTurma()

AVISO = "[!] Opção inválida."

def relatorios(opcao_usuario:int) -> None:
    if opcao_usuario == 1:
        relatorio.get_relatorio_escolas()
    elif opcao_usuario == 2:
        relatorio.get_relatorio_jogadores()
    elif opcao_usuario == 3:
        relatorio.get_relatorio_jogos()
    elif opcao_usuario == 4:
        relatorio.get_relatorio_turmas()
    elif opcao_usuario == 5:
        relatorio.get_relatorio_times_jogadores()
    elif opcao_usuario == 6:
        relatorio.get_relatorio_times()
    elif opcao_usuario == 7:
        relatorio.get_relatorio_numero_jogos()
    elif opcao_usuario == 0:
        return
    else:
        print(AVISO)


def inserir(opcao_usuario:int) -> None:
    if opcao_usuario == 1:
        nova_escola = controller_escola.inserir_registro()
    elif opcao_usuario == 2:
        novo_jogador = controller_jogador.inserir_registro()
    elif opcao_usuario == 3:
        nova_turma = controller_turma.inserir_registro()
    elif opcao_usuario == 4:
        novo_time = controller_time.inserir_registro()
    elif opcao_usuario == 5:
        novo_jogo = controller_jogo.inserir_registro()
    else:
        print(AVISO)


def atualizar(opcao_usuario:int) -> None:
    if opcao_usuario == 1:
        relatorio.get_relatorio_escolas()
        escola_atualizada = controller_escola.atualizar_registro()
    elif opcao_usuario == 2:
        relatorio.get_relatorio_jogadores()
        jogador_atualizado = controller_jogador.atualizar_registro()
    elif opcao_usuario == 3:
        relatorio.get_relatorio_turmas()
        turma_atualizada = controller_turma.atualizar_registro()
    elif opcao_usuario == 4:
        relatorio.get_relatorio_times()
        time_atualizado = controller_time.atualizar_registro()
    elif opcao_usuario == 5:
        relatorio.get_relatorio_jogos()
        jogo_atualizado = controller_jogo.atualizar_registro()
    else:
        print(AVISO)


def deletar(opcao_usuario:int) -> None:
    if opcao_usuario == 1:
        relatorio.get_relatorio_escolas()
        controller_escola.deletar_registro()
    elif opcao_usuario == 2:
        relatorio.get_relatorio_jogadores()
        controller_jogador.deletar_registro()
    elif opcao_usuario == 3:
        relatorio.get_relatorio_turmas()
        controller_turma.deletar_registro()
    elif opcao_usuario == 4:
        relatorio.get_relatorio_times()
        controller_time.deletar_registro()
    elif opcao_usuario == 5:
        relatorio.get_relatorio_jogos()
        controller_jogo.deletar_registro()
    else:
        print(AVISO)

if __name__ == "__main__":
    print(splash_screen.get_updated_screen())
    config.clear_console(2)

    while True:
        print(config.MENU_PRINCIPAL)
        opcao_usuario = int(input("Insira a opção desejada: "))
        config.clear_console(0.5)

        if opcao_usuario == 1:
            print(config.MENU_RELATORIOS)
            opcao_usuario_relatorio = int(input("Insira a opção do relatório desejado: "))
            config.clear_console(1)
            relatorios(opcao_usuario_relatorio)
            config.clear_console(0.5)

        elif opcao_usuario == 2:
            print(config.MENU_ENTIDADES)
            opcao_usuario_insercao = int(input("Insira a opção da entidade que deseja inserir: "))
            config.clear_console(1)
            inserir(opcao_usuario_insercao)
            config.clear_console(0.5)

        elif opcao_usuario == 3:
            print(config.MENU_ENTIDADES)
            opcao_usuario_atualizacao = int(input("Insira a opção da entidade que deseja atualizar: "))
            config.clear_console(1)
            atualizar(opcao_usuario_atualizacao)
            config.clear_console(0.5)

        elif opcao_usuario == 4:
            print(config.MENU_ENTIDADES)
            opcao_usuario_exclusao = int(input("Insira a opção da entidade que deseja deletar: "))
            config.clear_console(1)
            deletar(opcao_usuario_exclusao)
            config.clear_console(0.5)

        elif opcao_usuario == 5:
            print(splash_screen.get_updated_screen())
            config.clear_console(2)
            print("[+] Programa finalizado.")
            break

        else:
            print(AVISO)
            break