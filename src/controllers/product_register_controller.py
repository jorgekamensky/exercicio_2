from typing import Dict
from src.models.entities.product import Product
from src.models.repositories.products_repository import products_repository

class ProductRegister:
    def insert(self, new_product_information: Dict) -> Dict:
        try:
            product = self.__create_product_entity(new_product_information)
            self.__registry_product(product)
            response = self.__format_response(new_product_information)
            return response
        except:
            return {"success": False, "error": "Error in insert product"}
    
    def __create_product_entity(self, new_product_information: Dict) -> any:
        name = new_product_information["name"]
        flavor = new_product_information["flavor"]

        product = Product(name, flavor)
        return product
    
    def __registry_product(self, product: any) -> None:
        products_repository.insert_product(product)

    def __format_response(self, new_product_information: Dict) -> Dict:
        return{
            "success": True,
            "attributes": {
                "registry": 1,
                "name": new_product_information["name"],
                "flavor": new_product_information["flavor"]
            }
        }