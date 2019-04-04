from Usuario import Usuario
from datetime import datetime
import operator

mUsuarios = []

def carregarUsuariosDoArquivo():
    try:
        file = open("usuarios", "r")
        linhas = file.readlines()
        for linha in linhas:
            usuarioLido = Usuario(linha.split("|")[0], linha.split("|")[1], linha.split("|")[2],
                                    linha.split("|")[3], linha.split("|")[4], linha.split("|")[5])
            mUsuarios.append(usuarioLido)

        file.close()
    except:
        print("Nenhum usuario cadastrado.")


def cadastrarUsuario():
    print("\n\nCadastrar novo usuário")
    nome = input("   Nome do usuário: ")
    login = input("   Login: ")
    senha = input("   Senha: ")
    cargo = input("   Cargo: ")
    nivelAcesso = input("   Nível de acesso: ")
    dataHoraLogin = datetime.now().strftime("%Y-%m-%d %H:%M")
    usuario = Usuario(nome, login, senha, cargo, nivelAcesso, dataHoraLogin)

    mUsuarios.append(usuario)
    print("Quantidade" + str(len(mUsuarios)))
    salvarUsuariosNoArquivo()
    input()

def salvarUsuariosNoArquivo():
    file = open("usuarios", "w+")
    for i in mUsuarios:
        file.write("%s" % i)
    file.close()

def listarUsuarios():
    print("\n\n===================Usuários cadastrados===================\n")
    print("login  |  nome  |  cargo  |  nivel acesso  |  ultimo login")
    mUsuarios.sort(key=lambda x: x.nivelAcesso, reverse=False)
    # usuriosOrdenados = sorted(mUsuarios, key=operator.attrgetter('nivelAcesso'))
    for usuario in mUsuarios:
        print(usuario.login+ "  |  "+usuario.nome+ "  |  "+usuario.cargo+ "  |  "+usuario.nivelAcesso+ "  |  "+usuario.dataHoraLogin)
    print("\n===========================================================\n")
    print("\nTotal de usuários -> "+str(len(mUsuarios)))


def excluirUsuario(login):
    print("\n\nExcluir usuário")

def sair():
    print("\n========================")
    print("   Até logo!")
    print("========================\n")
    exit()