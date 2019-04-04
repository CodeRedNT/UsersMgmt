from enum import Enum

class Usuario:
    def __init__(self, nome, login, senha, cargo, nivelAcesso, dataHoraLogin):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.cargo = cargo
        self.nivelAcesso = nivelAcesso
        self.dataHoraLogin = dataHoraLogin

    def __str__(self):
        return self.nome+"|"+self.login+"|"+self.senha+"|"+self.cargo+"|"+self.nivelAcesso+"|"+self.dataHoraLogin


class NivelAcesso(Enum):
    SUPERUSUARIO = 0
    VISITANTE = 1
    USUARIO = 2
    ADMINISTRATIVO = 3
    TECNICO = 4
