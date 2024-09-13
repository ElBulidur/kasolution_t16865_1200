
def soma(num_1, num_2):
    return num_1 + num_2


# assert soma(10, 10) == 20, "O valor esperado era 20"

# print("função esta ok!")


import unittest

class TesteSimples(unittest.TestCase):

    def teste_soma(self):
        soma_5_4 = sum([5,4])

        self.assertEqual(soma_5_4, 9, "O valor esperado era 9.")


    def teste_nomes(self):
        nomes = ["Julio", "Ana", "Roberto"]

        self.assertEqual(len(nomes), 2, "É esperado apenas dois valores")


if __name__ == "__main__":
    unittest.main()
