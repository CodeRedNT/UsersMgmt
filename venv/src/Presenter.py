import Model
from datetime import datetime


def iniciarScript():
    Model.carregarUsuariosDoArquivo()

def cadastrarUsuario():
    Model.cadastrarUsuario()

def listarUsuarios():
    Model.listarUsuarios()
    input("\n\nPressione qualquer tecla para sair.")

def excluirUsuario():
    login = input("   Informe o login do usu￿ário que deseja excluir: ")
    if Model.consultarUsuario(login):
        Model.excluirUsuario(login)
    else:
        print("    -> Usuário não encontrado")
    input("Pressione qualquer tecla para continuar.")

def consultarUsuario():
    continuar = "S"
    while continuar == "S":
        login = input("   Informe o login do usu￿ário que deseja consultar: ")
        if not Model.consultarUsuario(login):
            print("    -> Usuário " + login+" não encontrado!" )
        continuar = input("Cadastrar outro usuário? (s/N): ").upper()


def listarSuperUsuarios():
    print("\nSuper-usuários cadastardos.")
    Model.listarSuperUsuarios()
    input("\n\nPressione qualquer tecla para sair.")


def consultarUsuariosPorData():
    data = input("Entre com a data que deseja recuparar os usuarios (dd/mm/aaaa): ")
    Model.consultarUsuarioPorData(data)
    input("\n\nPressione qualquer tecla para sair.")

def sairDoScript():
    Model.sair()
