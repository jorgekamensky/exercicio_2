import os
from typing import Dict

class ProductRegisterViews:
    def registry_product_view(self) -> str: # Isso indica um retorno como string? Pq o retorno esta como um dict?
        self.__clear()

        print("Cadastrar Novo Produto \n\n")
        name = input("Digite o nome do produto a ser cadastrado: ")
        flavor = input("Digite o sabor do produto: ")

        new_product_info = {"name": name, "flavor": flavor}

        return new_product_info
    
    def registry_product_success(self, product_registry: Dict) -> None:
        self.__clear()

        message = """
                Produto devidammente cadastrado
                *Infos:
                    Produto: {}
                    Sabor: {}
                """.format(product_registry["name"], product_registry["flavor"])
        print(message)

    def registry_product_fail(self, error: str) -> None:
        self.__clear()

        message = """
                    Erro ao cadastrar o Produto
                    {}
                  """.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')