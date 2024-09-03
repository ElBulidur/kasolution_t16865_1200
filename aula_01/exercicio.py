
# INTRODUÇÃO AO PYTHON
# OOP
# TIPAGEM DINÂMICA
# FUNCIONAL
# SAIDA DE INFORMAÇÃO => PRINT()
# ENTRADA DE INFORMAÇÃO => INPUT()


# VARIÁVEIS
# INTEIRO
# STRING
# BOLEANO
# REAL(Float)


# OPERADORES
# MATEMÁTICOS => +*/-
# LÓGICOS => AND, OR e NOT
# RELACIONAIS => ==, !=, >, >=, < E <=


# EXERCÍCIOS

"""
    Laboratório 1
        Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura.
        Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. Usar a formatação
        de interpolação.
"""

# nome, idade = input("Qual seu nome:"), input("Qual a sua idade:")
# peso, altura = input("Qual o seu peso:"), input("Qual a sua altura:")


# print("")
# print("#"*30)
# print("")

# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print(f"Peso: {peso}")
# print(f"Altura: {altura}")

"""
    Laboratório 2
        Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de
        divisão inteira e resto da divisão inteira, escrever um programa que solicite ao usuário um valor para saque e, a partir
        deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do
        saque.

        Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor
        quantidade possível de cédulas. 

"""

valor_para_saque = int(input("Coloque o valor para saque (Apenas multiplos de 5.): "))

c_50 = valor_para_saque // 50 # 2
valor_para_saque = valor_para_saque % 50 #35

c_20 = valor_para_saque // 20 # 1
valor_para_saque = valor_para_saque % 20 #15

c_10 = valor_para_saque // 10 # 1
valor_para_saque = valor_para_saque % 10 #5

c_5 = valor_para_saque // 5 # 1
valor_para_saque = valor_para_saque %5 #0

print(f"Resultado:\n {c_50} de 50\n {c_20} de 20\n {c_10} de 10\n {c_5} de 5")



