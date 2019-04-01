from Usuario import Usuario
from datetime import datetime
mUsuarios = []

def carregarUsuariosDoArquivo():
    try:
        file = open("usuarios", "r")
        linhas = file.readlines()
        mUsuarios = []
        for linha in linhas:
            usuarioLido = Usuario(linha.split("|")[0], linha.split("|")[1], linha.split("|")[2],
                                  linha.split("|")[3], linha.split("|")[4], linha.split("|")[5])
            mUsuarios.append(usuarioLido)
        file.close()
    except:
        print("erro")


def cadastrarUsuario():
    print("\n\nCadastrar novo usuário")
    nome = input("Nome do Usuario: ")
    login = input("Login: ")
    senha = input("Senha: ")
    cargo = input("Cargo: ")
    nivelAcesso = int(input("Nível de acesso: "))
    dataHoraLogin = datetime.now().strftime("%Y-%m-%d %H:%M")
    usuario = Usuario(nome, login, senha, cargo, nivelAcesso, dataHoraLogin)

    mUsuarios.append(usuario)
    print(len(mUsuarios))
    salvarUsuariosNoArquivo()
    input()

def salvarUsuariosNoArquivo():
    file = open("usuarios", "w+")
    for i in mUsuarios:
        file.write("%s\r\n" % i)
    file.close()

def listarUsuarios():
    for usuario in mUsuarios:
        print(usuario)


def excluirUsuario(login):
    print("\n\nExcluir usuário")

def sair():
    print("\n========================")
    print("   Até logo!")
    print("========================\n")
    exit()