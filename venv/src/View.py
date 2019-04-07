#!/usr/bin/python
import os
import sys
import Presenter


def montarMenu():
    opcao = 1
    Presenter.iniciarScript()
    while opcao != 0:
        print("Escolha uma das opções abaixo:\n")
        print("     1 - Listar usuários")
        print("     2 - Cadastrar novo usuário")
        print("     3 - Excluir usuário")
        print("     4 - Pesquisar usuário - por login")
        print("     5 - Pesquisar usuário - por data de acesso")
        print("     6 - Super usuários")
        print("     0 - Sair")

        try:
            opcao = int(input("\n\n Digite a opção desejada e tecle enter -> "))
        except:
            opcao = 0

        if opcao == 1:
            Presenter.listarUsuarios()
            limparTela()
        elif opcao == 2:
            Presenter.cadastrarUsuario()
            limparTela()
        elif opcao == 3:
            Presenter.excluirUsuario()
            limparTela()
        elif opcao == 4:
            Presenter.consultarUsuario()
            limparTela()
        elif opcao == 5:
            Presenter.consultarUsuariosPorData()
            limparTela()
        elif opcao == 6:
            Presenter.listarSuperUsuarios()
            limparTela()
        elif opcao not in [1-6]:
            Presenter.sairDoScript()


def limparTela():

    if identificarPlataforma() == "Linux":
        clear = lambda: os.system('clear')
    elif identificarPlataforma() == "Windows":
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')

    clear()


def identificarPlataforma():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]