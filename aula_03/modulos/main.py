# from operacoes import soma, subtracao, multiplicacao, divisao as dv

# import random as rd # apelido
from random import randint as rt
import time
import colorama as col

print(col.Fore.CYAN + "Julio Pereira")

from tqdm import tqdm

for i in tqdm(range(50), colour="red"):
    time.sleep(1)
else:
    print("Tempo esgotou!!!")

numero_aleatorios = rt(1,20)
# print(numero_aleatorios)

# print(random.random())
# sorte = random.randint(1, 10)

# while True:
#     numero = int(input("Adivinha o numero de 1 a 10: "))

#     if numero == sorte:
#         break

# for i in range(10):
#     print(1)
#     time.sleep(1)