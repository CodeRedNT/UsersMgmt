import Model

def iniciarScript():
    Model.carregarUsuariosDoArquivo()

def cadastrarUsuario():
    Model.cadastrarUsuario()

def listarUsuarios():
    Model.listarUsuarios()
    input("\n\nPressione qualquer tecla para sair.")

def excluirUsuario(login):
    print("\n\nExcluir usuário")

def sairDoScript():
    Model.sair()
