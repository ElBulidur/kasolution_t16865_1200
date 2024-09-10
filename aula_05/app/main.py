from pessoa_entity import Pessoa


# OBJETO
# julio = Pessoa("julio", 85, 1.72, 53)

# print(julio.nome)

# julio.nome_em_maiusculo()

# print(julio.nome)


print("="*80)
print("")
print("APP DE PESSOAS")

nome, peso  = input("Coloque o seu nome: "), int(input("Qual o seu peso: "))
altura, idade = float(input("E sua altura: ")), int(input("Por ultimo sua idade: "))


pessoa_1 = Pessoa(nome, peso, altura, idade)

criar_usuario = input("Você quer aproveitar e criar seu usuario? (sim/não)\n")

if criar_usuario == "sim":
    novo_usuario = input("Qual nome de usuário que você quer?\n")
    pessoa_1.criar_usuario(novo_usuario)
    

print(f"Sr {pessoa_1.nome}, seu cadastro foi realizado com sucesso!!!")

pessoa_1.usuario