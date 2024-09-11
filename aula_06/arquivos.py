import os


# try:
#     int("julio")
# except Exception as e:
#     log_file = open('log_erros.log', 'w')
#     log_file.write("Erros encontrados: \n")
#     log_file.write(f"{e}")
#     log_file.close()

alunos = [
    "Kleber",
    "Ana",
    "Roberto",
    "Talita"
]

# arquivo = open('lista_alunos.txt', 'w')

# arquivo.write("nome\n")

# for aluno in alunos:
#     arquivo.write(f"{aluno}\n")

# arquivo.close()


try:
    arquivo_para_ler = open("lista_alunos.txt", "r")

    # aluno = arquivo_para_ler.read() #Ler todo o arquivo
    # aluno = arquivo_para_ler.read(2) # pega parte do arquivo
    # aluno_2 = arquivo_para_ler.read(1)
    # aluno = arquivo_para_ler.readable() #Verificar se o arquivo esta aberto parea leitura
    # aluno = arquivo_para_ler.readline() #Ler a linha
    # aluno = arquivo_para_ler.readlines()

    # arquivo_para_ler.close()



    # for linha in arquivo_para_ler.readlines():
    #     if linha == "julio\n":
    #         print("Aluno encontrado")
    #     else:
    #         print("Não encontramos arquivos.")

    alunos_dicionarios = {}
    titulo = arquivo_para_ler.readline()
    alunos = arquivo_para_ler.readlines()

    for x in range(len(alunos)):
        if x+1 == len(alunos):
            aluno = alunos[x]
        else:
            aluno = alunos[x][:-1]

        alunos_dicionarios[f"{titulo[:-1]}_{x+1}"] = aluno

    print(alunos_dicionarios)



except Exception as e:
    raise ValueError(e)