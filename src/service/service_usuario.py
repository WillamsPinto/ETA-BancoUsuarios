from src.models.store import Store
from src.models.usuario import Usuario


class ServiceUsuario:
    def __init__(self):
        self.store = Store()

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

    def buscar_usuario(self, nome, profissao):
        for usuario in self.store.bd:
            if usuario.nome == nome and usuario.profissao == profissao:
                return True

        return False



    def delete_usuario(self, nome, profissao):

        if nome != None and profissao != None:
            if type(nome) == str and type(profissao) == str:
                if self.buscar_usuario(nome, profissao):
                    usuario = Usuario(nome, profissao)
                    self.store.bd.remove(usuario)
                    return "Usuario removido"
                else:
                    return "Usuario nao removido"

            else:
                return "Usuario nao removido"
        else:
            return "Usuario nao removido"