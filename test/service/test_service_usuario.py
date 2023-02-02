from src.service.service_usuario import ServiceUsuario


class TestServiceUsuario:

    #Adicionar Usuario
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

    #Buscar Usuario
    def test_buscar_usuario_nome_valido_profissao_valida(self):
        #Setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        service.add_usuario(nome_valido, profissao_valida)

        #chamada
        result = service.buscar_usuario(nome_valido, profissao_valida)

        #Avaliação
        assert result.nome == nome_valido
        assert result.profissao == profissao_valida

    def test_buscar_usuario_nome_invalido_profissao_valida(self):
        #Setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_valida = "Eng"
        service.add_usuario("Willams", profissao_valida)
        result_esperado = "Usuario não encontrado"

        #chamada
        result = service.buscar_usuario(nome_invalido, profissao_valida)

        #Avaliação
        assert result == result_esperado

    def test_buscar_usuario_nome_valido_profissao_invalida(self):
        #Setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_invalida = None
        service.add_usuario(nome_valido, profissao_invalida)
        result_esperado = "Usuario não encontrado"

        #chamada
        result = service.buscar_usuario(nome_valido, profissao_invalida)

        #Avaliação
        assert result == result_esperado

    def test_buscar_usuario_nome_invalido_profissao_invalida(self):
        #Setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_invalida = None
        service.add_usuario("Willams", "Eng")
        result_esperado = "Usuario não encontrado"

        #chamada
        result = service.buscar_usuario(nome_invalido, profissao_invalida)

        #Avaliação
        assert result == result_esperado


    #Alterar Usuario
    def test_alterar_usuario_newnome_valido_newprofissao_valida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        newNome_valido = "Talita"
        newProfissao_valido = "Dev"
        service.add_usuario(nome_valido, profissao_valida)
        result_esperado = "Usuario atualizado"

        # chamada
        result = service.change_usuario(nome_valido, profissao_valida, newNome_valido, newProfissao_valido)

        # avaliação
        assert result == result_esperado
        assert service.store.bd[0].nome == newNome_valido
        assert service.store.bd[0].profissao == newProfissao_valido

    def test_alterar_usuario_newnome_invalido_newprofissao_valida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        newNome_invalido = None
        newProfissao_valido = "Dev"
        service.add_usuario(nome_valido, profissao_valida)
        result_esperado = "Usuario não atualizado"

        # chamada
        result = service.change_usuario(nome_valido, profissao_valida, newNome_invalido, newProfissao_valido)

        # avaliação
        assert result == result_esperado
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valida

    def test_alterar_usuario_newnome_valido_newprofissao_invalida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        newNome_valido = "Talita"
        newProfissao_invalido = None
        service.add_usuario(nome_valido, profissao_valida)
        result_esperado = "Usuario não atualizado"

        # chamada
        result = service.change_usuario(nome_valido, profissao_valida, newNome_valido, newProfissao_invalido)

        # avaliação
        assert result == result_esperado
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valida

    def test_alterar_usuario_newnome_invalido_newprofissao_invalida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        newNome_invalido = None
        newProfissao_invalido = None
        service.add_usuario(nome_valido, profissao_valida)
        result_esperado = "Usuario não atualizado"

        # chamada
        result = service.change_usuario(nome_valido, profissao_valida, newNome_invalido, newProfissao_invalido)

        # avaliação
        assert result == result_esperado
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valida

    #Remover Usuario
    def test_remover_usuario_nome_valido_profissao_valida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_valida = "Eng"
        service.add_usuario(nome_valido, profissao_valida)
        result_esperado = "Usuario removido"
        store_esperado = []

        # chamada
        result = service.delete_usuario(nome_valido, profissao_valida)

        # avaliação
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_remover_usuario_nome_invalido_profissao_valida(self):
        # setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_valida = "Eng"
        service.add_usuario("Willams", profissao_valida)
        result_esperado = "Usuario não removido"
        store_empty = []

        # chamada
        result = service.delete_usuario(nome_invalido, profissao_valida)

        # avaliação
        assert result == result_esperado
        assert service.store.bd != store_empty

    def test_remover_usuario_nome_valido_profissao_invalida(self):
        # setup
        service = ServiceUsuario()
        nome_valido = "Willams"
        profissao_invalida = None
        service.add_usuario(nome_valido, "Eng")
        result_esperado = "Usuario não removido"
        store_empty = []

        # chamada
        result = service.delete_usuario(nome_valido, profissao_invalida)

        # avaliação
        assert result == result_esperado
        assert service.store.bd != store_empty

    def test_remover_usuario_nome_invalido_profissao_invalida(self):
        # setup
        service = ServiceUsuario()
        nome_invalido = None
        profissao_invalida = None
        service.add_usuario("Willams", "Eng")
        result_esperado = "Usuario não removido"
        store_empty = []

        # chamada
        result = service.delete_usuario(nome_invalido, profissao_invalida)

        # avaliação
        assert result == result_esperado
        assert service.store.bd != store_empty