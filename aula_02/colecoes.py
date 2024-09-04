# COLEÇÕES

# LISTA []
dados_usuario = ["Julio", 35, 1.76, True] #indice 

# print(type(dados_usuario))
# print(dados_usuario)
# print(dados_usuario[0]) # primeiro elemento
# print(dados_usuario[-1]) # ultimo elemento
# print(dados_usuario[len(dados_usuario)-1])
# print(dados_usuario[2:])
# print(dados_usuario[:3])
# dados_usuario[0] = "Julio Pereira"
# dados_usuario[0] = f"{dados_usuario[0]} Pereira"
# print(dados_usuario[0])

# RETORNA OU NÃO
# dados_usuario.append("São Paulo") # Adiciona um elemento no final da lista
# x = dados_usuario.clear() # limpa a lista (Não retorna)
# x = dados_usuario.copy() # retorna a copia da lista

# x = dados_usuario.count("Julio") # Retorna a quantidade de vez que o valor é encontrado.
# dados_usuario = [3,6,4,7,8,1,2]
# dados_usuario = ["Andre", "Julio"]
# dados_usuario.sort(reverse=True) # ordena.
# x = dados_usuario.pop(0) # Retorna o elemento pelo indice e retorna.
# x = dados_usuario.remove(35)

# print(x)
# print(dados_usuario)

# TUPLA ()
# meses = ("Jan", "Fev", "Mar", 3, True) # não modifica
dias = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")


# print(dias)
# print(dias[0])
# print(dias[:2])
# print(dias[-1])
# print(len(dias))

# x = dias.count("Seg")
# x = dias.index("Qua")


# DICIONÁRIO {}

dados_usuario_dicionario = { 
    "nome":"Julio Pereira",
    "Idade": 26,
    "Altura": 1.78,
    "Status": True
}

# print(dados_usuario_dicionario)
# print(dados_usuario_dicionario["nome"])
# print(dados_usuario_dicionario.get("nome"))

# print(dados_usuario_dicionario.keys())
# print(dados_usuario_dicionario.values())
# print(dados_usuario_dicionario.items())

# for x in dados_usuario_dicionario.items():
#     print(x)

dados_usuario_dicionario["Cidade"] = "São Paulo"

# print(dados_usuario_dicionario)


# MISTURANDO COLEÇÕES

curso = {
    "Escola": "Ka Solution",
    "Aluno": "Julio",
    "Notas": [1,4,5,6,7,8, {" bim1": 10, "bim2":7}],
    "Dias de Aula": ("Seg", "Qua", "Sex"),
    "Endereço": {
        "Endereço": "",
        "Numero": 123
    }
}

print(curso["Endereço"]["Numero"])
print(curso["Notas"][1])
print(curso["Notas"][-1]["bim2"])