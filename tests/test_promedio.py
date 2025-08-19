import unittest
import sys
import os

# Agrega el directorio padre a la ruta para encontrar el módulo 'calculadora'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora.promedio import calcular_promedio

class TestPromedio(unittest.TestCase):

    def test_promedio_lista_tipica(self):
        """Prueba el promedio de una lista de enteros positivos."""
        self.assertEqual(calcular_promedio([1, 2, 3, 4, 5]), 3.0)

    def test_promedio_con_negativos(self):
        """Prueba el promedio de una lista con números negativos."""
        self.assertEqual(calcular_promedio([-1, 1, -2, 2, 0]), 0)

    def test_promedio_con_flotantes(self):
        """Prueba el promedio de una lista de números de punto flotante."""
        self.assertAlmostEqual(calcular_promedio([1.5, 2.5, 3.5]), 2.5)

    def test_promedio_lista_un_elemento(self):
        """Prueba el promedio de una lista con un solo elemento."""
        self.assertEqual(calcular_promedio([10]), 10.0)

    def test_promedio_lista_vacia(self):
        """Prueba que una lista vacía arroja un ValueError."""
        with self.assertRaises(ValueError):
            calcular_promedio([])

if __name__ == '__main__':
    unittest.main()
