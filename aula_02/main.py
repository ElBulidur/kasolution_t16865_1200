# comandos de decisão

saque = 5

if saque%5 != 0:
    print("Saque não realizado. Tente novamente!!!")

    saque_novo = int(input("tente mais uma vez: "))
    
    if saque_novo%5 != 0: print("Saque não realizado!!!")
else:
    # print(saque)
    pass

nota = 6

# Se for abaixo de 6 esta REP
# Se for de 6 a 6.9 esta REC
# Se for acima de 7 esta APR

# if nota > 6.9:
#     print("O aluno esta APR")

# if nota < 6:
#     print("O Aluno esta REP")
# else:
#     print("O Aluno esta REC")

if nota < 6: 
    print("O Aluno esta REP")
elif nota > 6.9: 
    print("O aluno esta APR")
else: 
    print("O Aluno esta REC")

