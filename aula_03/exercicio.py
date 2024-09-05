"""
    Laboratório 1

    Neste laboratório será refeito o exercício do Caixa Eletrônico, apresentado no laboratório do Módulo 1. A
    diferença é que aqui deverá ser verificado se o valor do saque é múltiplo de 5. Se não for, apresentar uma
    mensagem informado da impossibilidade de realização do saque.

"""
valor_para_saque = 1#int(input("Coloque o valor para saque (Apenas multiplos de 5.): "))


tentativas = 3

while valor_para_saque%5 != 0:
    tentativas -= 1

    if tentativas <= 0:
        print("Tentativas esgotadas")
        break

    valor_para_saque = int(input(f"{tentativas}x - Deu Erro. Tente novamente: "))
else:
    cedulas = {
        "c50": valor_para_saque // 50,
        "c20": valor_para_saque % 50 // 20,
        "c10": valor_para_saque % 50 % 20 // 10,
        "c5": valor_para_saque % 50 % 20 % 10 // 5
    }

    print(f"Resultado:\n {cedulas['c50']} de 50\n {cedulas['c20']} de 20\n {cedulas['c10']} de 10\n {cedulas['c5']} de 5")


"""
    Laboratório 2

    Escrever um programa que solicite ao usuário:

        - O nome de um funcionário;
        - Seu salário.

    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% sobre o que ultrapassar R$ 5.000,00.
    No final, apresentar:

        - O nome do funcionário;
        - O salário bruto;
        - O valor do desconto;
        - O salário líquido.
"""

if 1 == 2: 
    try:

        funcionario = "" #input("Digite seu nome: ")

        salario = 10 #float(input("Digite o seu salário: "))

        desconto = 0

        if salario > 5000:
            desconto = (salario - 5000) * 0.1

        print("="*50)
        print("")
        print(f"Nome do Funcionário: {funcionario}")
        print(f"Salário Bruto: {salario}")
        print(f"Desconto: {desconto}")
        print(f"Salário liquido: {salario - desconto}")

    except NameError as n:
        print(f"Deu um erro de nome: {n}")
    except ValueError as v:
        print(f"Deu um erro de valor: {v}")
        # raise NameError("Deu erro de valor, mas eu forcei um erro de nome.")
        # pass