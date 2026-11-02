
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(8, 3), 11)


if __name__ == "__main__":
    unittest.main()
