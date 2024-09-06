

def soma(x, y):
    return x + y

somar = lambda x, y: x + y

somar_2 = lambda x, y: soma(x, y)

print(soma(2,5))

print(somar(2,5))
print(somar_2(2,5))

operacaoes_lista = [
    lambda x, y: x + y, 
    lambda x, y: x - y, 
    lambda x, y: x * y, 
    lambda x, y: x / y
]

print(operacaoes_lista[0](2,3))

operacoes = {
    "soma": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    "multiplicacao": lambda x, y: x * y,
    "divisao": lambda x, y: x / y
}

# print(operacoes["soma"](2,3))