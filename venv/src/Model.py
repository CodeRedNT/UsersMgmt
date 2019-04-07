from Usuario import Usuario
from datetime import datetime
import operator

mUsuarios = []


def carregarUsuariosDoArquivo():
    try:
        file = open("usuarios", "r")
        linhas = file.readlines()
        for linha in linhas:
            if linha.strip():
                usuarioLido = Usuario(linha.split("|")[0], linha.split("|")[1], linha.split("|")[2],
                                      linha.split("|")[3], linha.split("|")[4], linha.split("|")[5], linha.split("|")[6])
                mUsuarios.append(usuarioLido)

        file.close()
    except:
        print("Nenhum usuario cadastrado.")


def cadastrarUsuario():
    continuar = "S"
    while continuar == "S":
        print("\n\nCadastrar novo usuário")
        nome = input("   Nome do usuário: ")
        usuarioExiste = True
        while usuarioExiste:
            login = input("   Login: ")
            usuarioExiste = consultarUsuario(login)
            if usuarioExiste:
                print("    -> Usuário " + login + " já cadastrado. Informe outro login para este usuário.")

        senha = input("   Senha: ")
        cargo = input("   Cargo: ")
        print("   Níveis de acesso: ")
        print("       1 - Visitante")
        print("       2 - Usuário")
        print("       3 - Administrativo")
        print("       4 - Técnico")
        print("       5 - Super-Usuário")

        nivelAcesso = input("   Nível de acesso: ")
        dataLogin = datetime.now().strftime("%d/%m/%Y")
        horaLogin = datetime.now().strftime("h:%M")
        usuario = Usuario(nome, login, senha, cargo, nivelAcesso, dataLogin, horaLogin)

        mUsuarios.append(usuario)
        print("\nTotal de usuários na base -> " + str(len(mUsuarios)))
        continuar = input("Cadastrar outro usuário? (s/N): ").upper()
    salvarUsuariosNoArquivo()


def consultarUsuario(login):
    for usuario in mUsuarios:
        if usuario.login == login:
            print("    -> Usuário " + usuario.__str__())
            return True


def listarSuperUsuarios():
    count = 0
    for usuario in mUsuarios:
        if usuario.nivelAcesso == "5":
            count += 1
            print(usuario.__str__(), end="\n")
    print("\nTotal de Super-Usuários -> " + str(count))


def excluirUsuario(login):
    for usuario in mUsuarios:
        if usuario.login == login:
            mUsuarios.remove(usuario)
            salvarUsuariosNoArquivo()
            print("    -> Usuário " + login + "  exclúido com sucesso.")


def salvarUsuariosNoArquivo():
    file = open("usuarios", "w+")
    for i in mUsuarios:
        file.write("%s\n\r" % i)
    file.close()


def consultarUsuarioPorData(data):
    count = 0
    try:
        objetoData = datetime.strptime(data, '%d/%m/%Y')
        for usuario in mUsuarios:
            if datetime.strptime(usuario.dataLogin, '%d/%m/%Y') >= objetoData:
                count += 1
                print("    -> Usuário " + usuario.__str__())

        print("\nTotal de Usuários encontrados -> " + str(count))

    except:
        print("Data informada inválida")


def listarUsuarios():
    print("\n\n===================Usuários cadastrados===================\n")
    print("login  |  nome  |  cargo  |  nivel acesso  |  ultimo login")
    mUsuarios.sort(key=lambda x: x.nivelAcesso, reverse=False)
    for usuario in mUsuarios:
        print(
            usuario.login + "  |  " + usuario.nome + "  |  " + usuario.cargo + "  |  " + usuario.nivelAcesso + "  |  " + usuario.dataLogin+ "  |  " + usuario.horaLogin,
            end="")
    print("\n===========================================================\n")
    print("\nTotal de usuários (ordenado por nível de acesso) -> " + str(len(mUsuarios)))


def sair():
    print("\n========================")
    print("   Até logo!")
    print("========================\n")
    exit()
