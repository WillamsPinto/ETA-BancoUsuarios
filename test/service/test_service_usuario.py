from src.service.service_usuario import ServiceUsuario


class TestServiceUsuario:

    def test_add_usuario_nome_valido_profissao_valido(self): #nome e profissão válidos
        #setup
        service = ServiceUsuario()
        nome_valido = "Natalia"
        profissao_valido = "Eng"
        result_esperado = "Usuario adicionado"

        #chamada
        result = service.add_usuario(nome_valido, profissao_valido)

        #avaliação
        assert result == result_esperado
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valido

    def test_add_usuario_nome_invalido_profissao_valido(self): #nome invalido e profissão valido
        #setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_valido = "Eng"
        result_esperado = "Usuario invalido"
        store_esperado = []

        #chamada
        result = service.add_usuario(nome_invalido, profissao_valido)

        #avaliação
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_add_usuario_nome_valido_profissao_invalida(self): #nome valido e profissao invalida
        #setup
        service = ServiceUsuario()
        nome_valido = "Natalia"
        profissao_invalida = None
        result_esperado = "Usuario invalido"
        store_esperado = []

        #chamada
        result = service.add_usuario(nome_valido, profissao_invalida)

        #avaliação
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_add_usuario_nome_invalido_profissao_invalida(self): #nome e profissao invalidos
        #setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_invalida = None
        result_esperado = "Usuario invalido"
        store_esperado = []

        #chamada
        result = service.add_usuario(nome_invalido, profissao_invalida)

        #avaliação
        assert result == result_esperado
        assert service.store.bd == store_esperado

