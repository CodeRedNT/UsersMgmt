#!/usr/bin/python
import os
import sys
import Presenter
clear = lambda: os.system('clear')

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
            clear()
        elif opcao == 2:
            Presenter.cadastrarUsuario()
            clear()
        elif opcao == 3:
            clear()
        elif opcao not in [1-2]:
            Presenter.sairDoScript()
