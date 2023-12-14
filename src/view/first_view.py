def introduction_page():
    message = """
                ==Sistema de Gestao de Produtos e Clientes==

                1 - Cadastrar produto
                2 - Cadastrar cliente
                3 - Apresentar produtos cadastrados
                4 - Apresentar clientes de um determinado estado
                5 - Deletar um produto cadastrado
                6 - Sair
            """
    
    print(message)
    command = input("""
                Digite a opção: """)

    return command
