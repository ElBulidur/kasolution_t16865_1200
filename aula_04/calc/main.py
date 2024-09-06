from operacao import soma, subtrair, mult, divisao
from servicos import verificar_tipo
# from soma import soma
# from mult import mult
# from subtracao import subtrair
# from divisao import divisao
# import soma


def start():
    print("="*70)
    print("")

    print("Seja bem vindo a minha calculadora. Escolha uma das opções a seguir:")
    opcao = verificar_tipo(input("1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir: "))

    if opcao in (1, 2, 3, 4):
        num_1 = int(input("Digite o PRIMEIRO numero: "))
        num_2 = int(input("Digite o SEGUNDO numero: "))


        if opcao == 1:
            print(f"A soma dos numeros é: {soma(num_1, num_2)}")
        elif opcao == 2:
            print(f"A subtração dos numeros é: {subtrair(num_1, num_2)}")
        elif opcao == 3:
            print(f"A multiplicação dos numeros é: {mult(num_1, num_2)}")
        else:
            print(f"A divisão dos numeros é: {divisao(num_1, num_2)}")
    else:
        if opcao != None:
            print("O sistema só aceita de 1 a 4")

start()