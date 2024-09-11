"""
    Laboratório 1

    Escrever uma classe chamada Pessoa. Esta classe deve ter as propriedades:
         Nome;
         Idade;
         Peso;
         Altura.

    Definir também os seguintes métodos:
         getDados(): usado para retornar os dados da pessoa;
         setDados(): usado para atribuir todos os dados da pessoa;
         get_csv(): usado para retornar os dados da pessoa separados por ponto-e-vírgula (;) com o propósito
        de gerar um arquivo no formato CSV (o arquivo não será contemplado neste exercício).
"""

from pessoa_entity import PessoaDois, PessoaUm



pessoa_um = PessoaUm()

pessoa_dois = PessoaDois()

# print(PessoaUm)
# print(PessoaDois)

# print(pessoa_um) # 2 COLUNAS
# print(pessoa_dois) # 0 COLUNAS


# print(pessoa_um.nome)
pessoa_dois.setDados("julio", 84)
print(pessoa_dois.getDados())