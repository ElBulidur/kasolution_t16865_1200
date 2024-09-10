# ABSTRAÇÃO
class Pessoa:
    def __init__(self, nome:str, peso, altura, idade):
        self.nome = nome.upper()
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.usuario = ""

    def nome_em_maiusculo(self):
        self.nome = self.nome.upper()
    
    def criar_usuario(self, usuario):
        self.usuario = usuario
        print("Usuario criado com sucesso!!!\n\n")

    

