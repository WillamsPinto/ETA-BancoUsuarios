from src.models.store import Store
from src.models.usuario import Usuario
from src.service.service_usuario import ServiceUsuario

usuario = Usuario("Natalia", "Eng")

print(usuario)
print(usuario.nome)
print(usuario.profissao)

usuario = Usuario("Thales", "Jornalista")

print(usuario)
print(usuario.nome)
print(usuario.profissao)


store = Store()
#print(store.bd)

service = ServiceUsuario()
print(service.store.bd)

result = service.add_usuario("Natalia", "Eng")
print(result)

result = service.add_usuario(None, "Eng")
print(result)

result = service.add_usuario("Natalia", None)
print(result)

print(service.store.bd)

