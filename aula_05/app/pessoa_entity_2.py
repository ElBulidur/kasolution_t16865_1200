
class PessoaDois:
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, p_nome: str):
        self.__nome = p_nome.upper()

    def nome_em_maiusculo(self):
        self.nome = self.nome.upper()
