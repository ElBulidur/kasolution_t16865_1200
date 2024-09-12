import requests, json


### CRUD API

# READ
endpoint = "https://66e36762494df9a478e51e49.mockapi.io/"
recurso ="alunos"
id = 2

endereco_completo = endpoint + recurso


def ler_api(url):
    resposta = requests.get(url=url)

    if resposta.status_code == 200:
        conteudo = json.loads(resposta.content)
        return conteudo
    

# alunos = ler_api(endereco_completo)


def pegar_aluno_por_id(url, id):
    resposta = requests.get(url=f"{url}/{id}")

    if resposta.status_code == 200:
        conteudo = json.loads(resposta.content)

        return conteudo
        

# aluno = pegar_aluno_por_id(endereco_completo, id)

dados_para_cadastrar_ou_atualizar = {
  "nome": "Ana Clara",
  "email": "clarinhagv@email.com"
}

def criar_aluno_na_api(dados):
    resposta = requests.post(endereco_completo, data=dados)

    if resposta.status_code == 201:
        aluno_criado = json.loads(resposta.content)
        print(f"O aluno {aluno_criado['nome']} foi criado com sucesso!")


# criar_aluno_na_api(dados_para_cadastrar_ou_atualizar)

def atualizar_aluno_pela_api(url, id, dados):

    resposta = requests.put(url=f"{url}/{id}", data=dados)

    if resposta.status_code == 200:
            aluno_criado = json.loads(resposta.content)
            print(f"O aluno {aluno_criado['nome']} foi atualizado com sucesso!")


# atualizar_aluno_pela_api(endereco_completo, id, dados_para_cadastrar_ou_atualizar)


def deletar_aluno_pela_api(url, id):
    resposta = requests.delete(url=f"{url}/{id}")

    if resposta.status_code == 200:
        aluno_criado = json.loads(resposta.content)
        print(f"O aluno {aluno_criado['nome']} foi deletado com sucesso!")
    else:
        print(f"{resposta.status_code} - Não foi encontrado nenhum aluno com este ID.")

# deletar_aluno_pela_api(endereco_completo, id)