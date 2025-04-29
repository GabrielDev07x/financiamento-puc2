import unittest

from financiamento.calculadoraSimples import somar, subtrair  # Ajuste a importação

#alterações
class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(1, 2), 3)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(2, 1), 1)
        self.assertEqual(subtrair(1, 2), -1)
        self.assertEqual(subtrair(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
