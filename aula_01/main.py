# COMENTÁRIOS

# print("Ola mundo")

"""
nome = input("Coloque o seu nome: ")

print(f"Seu nome é: {nome}")

"""
'''
  comentário em bloco...
'''

# VARIÁVEIS
# tipagem dinâmica

x = 10  # Inteiro (Int)
nome = "Julio" # texto (String)
altura = 1.72 # Real (Float)
aprovado = True # Boleano (ou lógica)

# print(f'x = {x}, tipo = {type(x)}')
# print(type(x) == int)
# print(f'nome = {nome}, tipo = {type(nome)}')
# print(type(nome) == str)
# print(f'altura = {altura}, tipo = {type(altura)}')
# print(type(altura) == float)

# novo_tipo_altura = str(altura) # castear
# print(f'novo_tipo_altura = {novo_tipo_altura}, tipo = {type(novo_tipo_altura)}')
# print(type(novo_tipo_altura) == float)

# ATRIBUIÇÕES MULTIPLAS

v_1 = v_2 = v_3 = 10
# print(f"v1={v_1}, v2={v_2}, v3={v_3}")

# ATRIBUIÇÕES SEQUENCIAIS

# cliente, cpf, posicao = "Julio Pereia", 312345465, 1.23

# print(f"Cliente: {cliente}, com cpf {cpf} esta na posição {posicao}")



# TRABALHANDO COM STRING

empresa = "Ka Solution"

# print(empresa[0:2])
# print(empresa[-2:])

# print(   len(empresa)     )
# print(empresa[len(empresa)-2:len(empresa)])

primeiro, segundo = empresa.split(" ")

# print(primeiro)
# print(segundo)

# print( len(empresa.split(" "))  )
# print( empresa.split(" ")[1]  )


nome = "Julio Pereira"

# # print(  nome.find("Pereira") )
# print(  nome.find("Juli", 0, 4) )


# OPERADORES

# matemático
n_1 = 10
n_2 = 2
n_3 = 11
n_4 = 2

# print( n_1 + n_2  ) # adição
# print( n_1 - n_2  ) # subtração
# print( n_1 / n_2  ) # divisão
# print( n_1 * n_2  ) # multiplacação

# print( n_3 / n_4  ) # divisão real
# print( n_3 // n_4  ) # divisão inteira
# print( n_3 % n_4  ) # resto da divisão inteira

# Forma reduzida

# n_1 = n_1 + 2
# n_1 += 2


# n_1 = n_1 / n_4
n_1 /= n_4
# print( n_1)


# relacionais
# print( n_1 == n_2 ) # False
# print( n_1 != n_2 ) # True
# print( n_1 > n_2 ) # True
# print( n_1 >= n_2 ) # True
# print( n_1 < n_2 ) # False
# print( n_1 <= n_2 ) # False

# logicos
print( n_1 == n_2  and n_1 != n_3    ) # False e True
print( n_1 == n_2  or n_1 != n_3    ) # False e True
print(not n_1 == n_2  or n_1 != n_3    ) # False e True




