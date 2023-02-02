from src.models.store import Store
from src.models.usuario import Usuario


class ServiceUsuario:
    def __init__(self):
        self.store = Store()

    def verificar_usuario(self, nome, profissao):
        for usuario in self.store.bd:
            if usuario.nome == nome and usuario.profissao == profissao:
                return True
        return False

    def buscar_usuario(self, nome, profissao):
        for usuario in self.store.bd:
            if usuario.nome == nome and usuario.profissao == profissao:
                return usuario
        return "Usuario não encontrado"

    def add_usuario(self, nome, profissao):
        if nome != None and profissao != None:
            if type(nome) == str and type(profissao) == str:
                usuario = Usuario(nome, profissao)
                self.store.bd.append(usuario)
                return "Usuario adicionado"
            else:
                return "Usuario invalido"
        else:
            return "Usuario invalido"

    def change_usuario(self, nome, profissao, newName, newProfissao):
        if type(nome) == str and type(profissao) == str and nome != None and profissao != None and newName != None and newProfissao != None:
            if self.verificar_usuario(nome, profissao):
                usuario = Usuario(newName, newProfissao)
                self.store.bd[self.store.bd.index(self.buscar_usuario(nome, profissao))] = usuario
                return "Usuario atualizado"
            else:
                return "Usuario não atualizado"
        else:
            return "Usuario não atualizado"

    def delete_usuario(self, nome, profissao):
        if type(nome) == str and type(profissao) == str and nome != None and profissao != None:
            if self.verificar_usuario(nome, profissao):
                self.store.bd.remove(self.buscar_usuario(nome, profissao))
                return "Usuario removido"
            else:
                return "Usuario não removido"
        else:
            return "Usuario não removido"