
class Soma:
    def __init__(self, *args):
        self.valores = self.__tratar_valores(args)
        self.resultado = sum(self.valores[0])

    def __tratar_valores(self, valores):
        valores_corrigido = []
        valores_nao_aceito = []

        for valor in valores:
            try:
                if type(valor) != int:
                    valores_corrigido.append(int(valor))
                else:
                    valores_corrigido.append(valor)

            except:
                valores_nao_aceito.append(valor)
                continue

        return valores_corrigido, valores_nao_aceito
    
    def resultado_final(self):
        print(f"Numeros possivéis para soma: {self.valores[0]}")
        print(f"Numeros que não pode somar: {self.valores[1]}")
        
        print(f"A soma dos numeros é: {self.resultado}")



class Subtracao:
    pass

class Divisao:
    pass

class Multiplicacao:
    pass