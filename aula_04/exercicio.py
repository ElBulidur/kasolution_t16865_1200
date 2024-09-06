"""    
    Laboratório 1

        Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, o usuário deverá fornecer 5 nomes
        a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.

"""

# lista = list()

# for x in range(5):
#     nome = input(f"Escreva o {x+1}° nome: ")
#     lista.append(nome) # RETORNA OU MODIFICA

# lista.sort()

# print(lista)

# lista = [input(f"Escreva o {x+1}° nome: ") for x in range(5)]

# lista.sort()

# print(lista)




"""
    Laboratório 2

        Neste laboratório, uma lista de 100 números será criada de forma aleatória, ou seja, os elementos serão números
        aleatórios.
        Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que
        10.

"""


# import random as rn
from random import random as rn, randint as rni


# numeros_maiores_que_10 = []

# for x in range(100):
#     numero = rni(0, 101)

#     if numero > 10:
#         numeros_maiores_que_10.append(numero)

# numeros_maiores_que_10.sort()


print(f"Os numeros gerados maiores que 10 são: {[x for x in [rni(0, 101) for x in range(100)] if x > 10]}")



