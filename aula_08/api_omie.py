import requests
import json


app_key ="4974205025790"

app_secret = "f63d7e796b51c301934b2d40ae675623"

endpoint = "https://app.omie.com.br/api/v1/geral/clientes/"


headers = {
    'Content-type': 'application/json'
}

data = {
    "call":"AlterarCliente",
    "app_key":app_key,
    "app_secret":app_secret,
    "param":[
        {
            "codigo_cliente_integracao":"CodigoInterno0001",
            "email":"primeiro@ccliente.com.br",
            "razao_social":"Primeiro Cliente  Ltda Me",
            "nome_fantasia":"Primeiro Cliente"
        }
    ]
}

auth = {
    "Basic": {
        "Username": "",
        "Password": ""
    }
}

resposta = requests.post(url=endpoint, data=json.dumps(data), headers=headers)

print(json.loads(resposta.content))

