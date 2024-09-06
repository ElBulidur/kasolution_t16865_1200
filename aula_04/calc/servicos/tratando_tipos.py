

def verificar_tipo(valor:str):
    if not valor.isdigit():
        print("tem que ser digito.")
        return None
    else:
        return int(valor)