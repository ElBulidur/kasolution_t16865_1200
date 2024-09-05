# JA VIMOS


# VARIÁVEIS
# OPERADORES
# COLEÇÕES
# ESTRUTURA CONDICIONAL

# ESTRUTURA DE REPETIÇÃO


for x in [1, 2, 3, 4, 5]:
    # print(x)
    pass

for x in range(5):
    # print(x)
    pass

for x in range(1,5):
    # print(x)
    pass

for x in range(1,10, 2):
    # print(x)
    pass


nome_completo = "Julio Cezar Pereira"

for x in nome_completo.split(" "):
    # print(x)
    pass

nome = "julio" #5

for i in range(len(nome)):
    # print(i)
    if nome[i] in ['k', 'l', 'o']:
        # print(nome[i].capitalize())
        nome = nome.replace(nome[i], nome[i].capitalize())

        break

# print(nome)

curso = {
    "Nome": "Programando com Python",
    "Turma": "001",
    "Alunos": ["Paulo", "Raul", "Beatriz"]
}

for key in curso.keys():
    # print(key)
    if key == "Alunos":
        for element in curso[key]:
            # print(element)
            pass

for value in curso.values():
    # print(value)
    pass

for items in curso.items():
    # print(items[0])
    pass

for key, value in curso.items():
    # print(f"A chave '{key}' tem o valor: {value}")
    pass

colunas_que_quero = [x for x in curso.keys() if x in ['Nome', 'Alunossds']]

# print(colunas_que_quero)


# for x in nome: print(x)

# WHILE

x = 0

while x < 1:
    # print("10")
    x += 1

numero = 1
numero_da_sorte = 7

while numero == 0:
    numero_usuario = int(input("Adivinha o número: "))

    if numero_usuario == numero_da_sorte:
        numero += 1
        print("Acertouuu. Showww!!!")


while True:
    numero_usuario = int(input("Adivinha o número: "))

    if numero_usuario == numero_da_sorte:
        break
    else:
        continue        