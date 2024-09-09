"""
    Laboratório 3

    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:

        -  Até 17 anos - R$ 50,00;
        - Entre 18 e 59 anos - R$ 60,00;
        - A partir de 60 anos - R$ 20,00.

    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
"""
# associado
# ingresso

associado = ''#input("Nome do associado: ")
idade = 2#int(input("Qual a idade: "))
ingresso = 50.00

if idade <= 17:
    ingresso = 50.00
elif idade <= 59:
    ingresso = 60.00
else:
    ingresso = 20.00

# print(f"Associado: {associado} e valor do ingresso: {ingresso}")


"""
    Laboratório 4

    Neste laboratório, o usuário fornece as informações: dia, mês e ano.
    Com base nestas informações, determinar quantos dias restam para terminar o ano informado.
    Realizar as validações:

    - O mês informado deve estar na faixa entre 1 e 12;
    - O dia informado deve ser compatível com o mês informado;
    - Usar o ano para determinar o número de dias do mês de fevereiro.
"""

dia = 28
mes = 11
ano = 2023

if mes < 1 or mes > 12:
    raise ValueError("Precisa ser o valor de 1 a 12.")

dias_fev = 29 if ano%4 == 0 else 28

dias_do_mes = (31, dias_fev, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

if dia < 1 or dia > dias_do_mes[mes-1]: 
    raise ValueError("Dia fora do mês informado!")

dias_restantes_do_mes = dias_do_mes[mes-1] - dia

for x in range(mes,12):
    dias_restantes_do_mes += dias_do_mes[x]

print(f"Faltam {dias_restantes_do_mes} dias do ano informado.")