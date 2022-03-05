def print_header_footer(fun):
    def wrapper(*args,**kwargs):
        print("///------------Header----------------///")
        fun(*args, **kwargs)
        print("////-----------Footer----------///")
    return wrapper

@print_header_footer
def suma(a: int, b: int):
    print("La suma es: "+ str(a+b))

@print_header_footer
def menu():
    detalle="""
            MENU DEL DIA
        1. Pescado
        2. Carne
        3. Pollo
    """
    print(detalle)

suma(5,10)
menu()
