import os

# arquivo = "..\\aula_06\\lista_alunos.txt"
# arquivo = r"..\aula_06\lista_alunos.txt"
arquivo = "../aula_06/lista_alunos.txt"

# if os.path.exists(arquivo): #verificar se o arquivo existe
#     print("arquivo já existe")
# else:
#     print("Arquivo não existe na pasta")

caminho_pasta = "../aula_06"

# if os.path.isdir(caminho_pasta): #verificar se é  pasta
#     print("Sim esta é uma pasta")
# else:
#     print("Não é uma pasta")

# print( os.getcwd() ) #printar o local exato do arquivo


# os.chdir("../aula_06") # navegar a o caminho especifico


# print("depois do chdir: "+ os.getcwd() )

# os.mkdir("JULIO") # Cria pasta

# os.rmdir("JULIO") # Deleta pasta

# os.remove("../aula_06/teste.txt") #Remover arquivo

# files_and_folders = os.listdir()
# arquivos = []
# pastas = []
# caminho_atual = os.getcwd()


# for x in files_and_folders:
#     if os.path.isfile(f"{caminho_atual}/{x}"):
#         arquivos.append(x)
#     else:
#         pastas.append(x)


# print(f"Tem {len(arquivos)} arquivos e {len(pastas)} pastas")

from pathlib import Path

# caminho = Path("c/projetos_python/kasolution_t16865_1200/aula_06/lista_alunos.txt")
# print(caminho.suffix[1:])

# CSV
import csv

alunos_novos = [
    ["Julio", "julio@email.com"],
    ["Roberta", "roberta@email"]
]


arquivo_csv = open("alunos_novo.csv", "w")

gravar = csv.writer(arquivo_csv, delimiter=",", lineterminator="\n")
gravar.writerow(["Nome", "Email"])
gravar.writerows(alunos_novos)

arquivo_csv.close()


with open("alunos_novo.csv", "r") as csv_alunos:
    lendo_csv = csv.reader(csv_alunos, delimiter=',')

    for linha in lendo_csv:
        # print(linha)
        pass



# EXCEL
import openpyxl
import xlrd

pasta_para_xlrd = xlrd.open_workbook("tab2011.xls")
planilha = pasta_para_xlrd.sheet_by_index(0)


for idx in range(planilha.nrows):
    row = planilha.row(idx)
    # print(row)


pasta_para_openpyxl = openpyxl.load_workbook(filename="palinhas_vendas.xlsx")

linhas = []

for dados in pasta_para_openpyxl["Obj, Metas, Ind. e Res. Interm."].iter_rows(values_only=True):
    linhas.append(dados)

# print(linhas[0][0] == 'Programas no Plano Plurianual 2020-2023, de responsabilidade do Ministério da Defesa')


import pandas as pd




















