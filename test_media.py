import unittest

def calcular_media(nota1, nota2, nota3):
    for nota in (nota1, nota2, nota3):
        if not isinstance(nota, (int, float)):
            raise ValueError("Todas as notas devem ser numéricas.")
        if nota < 0:
            raise ValueError("As notas não podem ser negativas.")
    
    return (nota1 + nota2 + nota3) / 3


class TestMedia(unittest.TestCase):
    
    def test_media_notas_normais(self):
        self.assertEqual(calcular_media(7, 8, 9), 8.0)

    def test_media_todas_as_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_media_notas_maximas(self):
        self.assertEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_notas_decimais(self):
        self.assertEqual(calcular_media(6.5, 7.5, 8.0), 7.333333333333333)

    def test_media_notas_invalidas(self):
        with self.assertRaises(ValueError):
            calcular_media("a", 8, 9)

if __name__ == '__main__':
    unittest.main()
