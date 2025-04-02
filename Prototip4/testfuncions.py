import unittest

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

class TestFuncions(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 5), -5)
        self.assertEqual(resta(-2, -3), 1)

    def test_divideix(self):
        self.assertEqual(divideix(6, 2), 3)
        self.assertEqual(divideix(9, -3), -3)
        self.assertEqual(divideix(10, 0), "Error: divisió per zero")

if __name__ == "__main__":
    unittest.main()
