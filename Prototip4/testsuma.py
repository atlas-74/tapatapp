import unittest

def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(-5, -3), -8)
        self.assertEqual(suma(10, -10), 0)

if __name__ == "__main__":
    unittest.main()