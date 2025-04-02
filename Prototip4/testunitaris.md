Tests Unitaris

Què són els tests unitaris?

Els tests unitaris són un tipus de proves de programari que s'enfoquen a verificar el funcionament correcte de components individuals d'una aplicació, com ara funcions, mètodes o classes. L'objectiu principal dels tests unitaris és assegurar que cada unitat de codi funcioni segons el disseny esperat abans d'integrar-la amb altres parts del sistema.

Aquests tests són essencials per a la detecció primerenca d'errors, la millora de la qualitat del codi i l'agilització del procés de desenvolupament.

Llibreries de test amb Python

Python ofereix diverses llibreries per realitzar tests unitaris. Algunes de les més populars són:

unittest: Forma part de la llibreria estàndard de Python i proporciona eines per a la creació i execució de tests unitaris.

pytest: Una llibreria més avançada i flexible que permet escriure tests amb menys codi i facilita la integració amb altres eines.

nose2: Successor de nose, una llibreria que amplia les funcionalitats de unittest.

doctest: Permet escriure tests dins de la documentació de les funcions mitjançant exemples d’ús.

Funcionament de la llibreria unittest

La llibreria unittest de Python segueix un enfocament basat en classes per a definir i executar tests. A continuació es mostra un exemple bàsic de com utilitzar-la:

import unittest

# Funció a provar
def suma(a, b):
    return a + b

# Classe de test
class TestSuma(unittest.TestCase):
    def test_suma_positius(self):
        self.assertEqual(suma(2, 3), 5)
    
    def test_suma_negatius(self):
        self.assertEqual(suma(-1, -1), -2)
    
    def test_suma_mixta(self):
        self.assertEqual(suma(-1, 1), 0)

# Executar els tests
if __name__ == '__main__':
    unittest.main()

Explicació:

Importem unittest.

Creem una funció (suma) que volem provar.

Definim una classe de test que hereta de unittest.TestCase.

Implementem diferents casos de prova mitjançant el mètode assertEqual.

Finalment, si el fitxer s'executa directament, es crida unittest.main() per executar els tests.

Amb unittest, podem automatitzar les proves i assegurar-nos que els canvis al codi no introdueixin errors involuntaris.

# Assertions més importants en `unittest`

En `unittest`, les assertions s'utilitzen per comprovar si el codi es comporta com s'espera. Aquí tens una llista de les més importants i la seva utilitat:

## Assertions bàsiques

- `assertEqual(a, b)`: Verifica que `a == b`.
- `assertNotEqual(a, b)`: Verifica que `a != b`.
- `assertTrue(x)`: Comprova que `x` és `True`.
- `assertFalse(x)`: Comprova que `x` és `False`.
- `assertIs(a, b)`: Comprova que `a` i `b` són el mateix objecte.
- `assertIsNot(a, b)`: Comprova que `a` i `b` NO són el mateix objecte.

## Assertions per llistes i col·leccions

- `assertIn(a, b)`: Comprova que `a` està dins de `b`.
- `assertNotIn(a, b)`: Comprova que `a` NO està dins de `b`.
- `assertCountEqual(a, b)`: Comprova que les col·leccions `a` i `b` tenen els mateixos elements (independentment de l'ordre).

## Assertions per excepcions

- `assertRaises(exc, func, *args, **kwargs)`: Comprova que `func(*args, **kwargs)` llença l'excepció `exc`.
- `assertRaisesRegex(exc, regex, func, *args, **kwargs)`: Comprova que l'excepció `exc` llençada per `func` conté el text indicat per `regex`.

## Assertions per tipus i objectes

- `assertIsInstance(obj, cls)`: Comprova que `obj` és una instància de la classe `cls`.
- `assertNotIsInstance(obj, cls)`: Comprova que `obj` NO és una instància de `cls`.

## Assertions per comparació numèrica

- `assertGreater(a, b)`: Comprova que `a > b`.
- `assertGreaterEqual(a, b)`: Comprova que `a >= b`.
- `assertLess(a, b)`: Comprova que `a < b`.
- `assertLessEqual(a, b)`: Comprova que `a <= b`.

Aquestes assertions són fonamentals per assegurar que els tests en `unittest` validen correctament el comportament del codi!