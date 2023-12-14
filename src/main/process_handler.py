from .constructor.introduction_process import introduction_process
from .constructor.product_register_constructor import product_register_process

def start():
    while True:
        command = introduction_process()
        if command == '1': product_register_process()
        else: exit()