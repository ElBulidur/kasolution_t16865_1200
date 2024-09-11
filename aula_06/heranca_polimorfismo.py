from pessoa_entity import PessoaDois, PessoaUm

# class Aluno(PessoaUm): 
#     def __init__(self, nome): 
#         super().__init__(nome.upper())

# POLIMORFISMO
class Aluno(PessoaDois): 
    def getDados(self):
        dados = f'Dados Aluno {super().getDados()}'
        return dados  

aluno_1 = Aluno()

# aluno_1.nome = "Vermelho"
# aluno_1.idade = 10

# nome =23

aluno_1.setDados("Julio", 23)

print( aluno_1.getDados() )
# aluno_1.setDados("Julio", 12)
# print(aluno_1.getDados())

