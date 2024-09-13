from .crud_api import ler_api
from .banco_de_dados_1 import cadastrar_aluno

endpoint = "https://66e36762494df9a478e51e49.mockapi.io/alunos"


alunos = ler_api(endpoint)

for aluno in alunos:
    cadastrar_aluno(aluno['nome'], aluno['email'])


        