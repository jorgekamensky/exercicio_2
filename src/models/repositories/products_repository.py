from typing import List

class __ProductsRepository:
    def __init__(self) -> None:
        self.__products_list = []

    def insert_product(self, product: any) -> None:
        self.__products_list.append(product)

    def return_all_products(self) -> List:
        return self.__product_list
    
    def delete_products(self, product: any) -> None:
        self.__products_list.remove(product)

products_repository = __ProductsRepository