# MODULOS
# FUNÇÕES
# OOP / POO

# PARADIGMA DA PROGRAMAÇÃO

# ABSTRAÇÃO
# MEMÓRIA <= OBJETO
# ATRIBUTOS / MÉTHODOS




# ABSTRAÇÃO (Classe)
class Copo:
    def __init__(self) -> None:
        self.cor = "Vermelho"
        self.tipo = "Americano"
        self.estado = "limpo"

    def sujar(self):
        self.estado = "sujo"


# print(Copo)
# OBJETO
meu_copo = Copo()
meu_copo_2 = Copo()

# print(meu_copo)

# ATRIBUTO
# print(meu_copo.cor)

meu_copo.cor = "Amarelo"

# print(meu_copo.cor)

# print(meu_copo_2.cor)

# MÉTODOS

print(f"Pegue o copo 2 e ele estava {meu_copo_2.estado}")

print("Usei ele....")

meu_copo_2.sujar()

print(f"Agora ele esta {meu_copo_2.estado}")