
class PessoaUm:
    def __init__(self, nome):
        # ATRIBUTO
        self.nome = nome
        self.peso = 0


class PessoaDois:
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, p_nome:str):
        self.__nome = p_nome.upper()

    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, p_peso):
        self.__peso = p_peso

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, p_altura):
        self.__altura = p_altura

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, p_idade):
        self.__idade= p_idade


    def getDados(self):
        return self.nome, self.idade, self.peso, self.altura
    
    def setDados(self, nome, idade, peso=None, altura=None):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.idade = idade


    def get_csv(self):
        return f"{self.nome};{self.peso};{self.altura};{self.idade};"


