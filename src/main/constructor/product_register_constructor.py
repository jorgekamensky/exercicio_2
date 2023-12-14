from src.controllers.product_register_controller import ProductRegister
from src.view.product_register_view import ProductRegisterViews

def product_register_process():
    product_register_view = ProductRegisterViews()
    product_register_controller = ProductRegister()

    new_product_information = product_register_view.registry_product_view()
    response = product_register_controller.insert(new_product_information)

    if response["success"]:
        product_register_view.registry_product_success(response["attributes"])
    else:
        product_register_view.registry_product_fail(response["error"])