
# REPETIÇÃO
# FOR
# WHILE
# TRATAMENTO
# TRY/EXECEPT
# MODULOS
# FUNÇÕES

# DECLARAÇÃO
def imprime_bemvindo():
    print("Seja bem vindo!!!")
    
def retorna_msg():
    return "Seja bem vindo com retorno"

# UTILIZAÇÃO
# imprime_bemvindo()



# NÃO RETORNA
# RETORNA

# res = retorna_msg()



# PARAMETROS

# retorna e com mparametro
def somar_mais_10(numero):
    return numero + 10

# com parametros e inferencia
def imprime_em_maiusculo(texto:str):
    try:
        print(texto.upper())
    except:
        pass


# res = somar_mais_10(17)

# print(res)

# imprime_em_maiusculo("julio")

# num = int(input("digite um numero"))

# print( somar_mais_10(num) )


# COM PARAMETRO OPCIONAL
def subtrair_descontos(valor, desconto=0):
    return valor - desconto

# print( subtrair_descontos(200, 50) )

def pegar_maior_e_menor_numero(lista:list):
    lista.sort()
    maior = lista[-1]
    menor = lista[0]

    return maior, menor


numeros = [2, 3, 5,7,32,9]


# res = pegar_maior_e_menor_numero(numeros)
x, y = pegar_maior_e_menor_numero(numeros)

# print(x)
# print(y)

def carrinho_de_compra(*args):
    print(args)
    # return sum(args)


# print( carrinho_de_compra(12, 89, 452) )


def calcular_imposto(**kargs):
    print(kargs.get('ipva'))

    if kargs.get('ipva'):
        print("Tem IPVA")
    

# calcular_imposto(dpvat=20, iptu=12, ipva=300)