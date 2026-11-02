
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(8, 3), 11)

    def test_sub(self):
        calculator = Calculator()
        self.assertEqual(calculator.sub(8, 3), 5)
        self.assertEqual(calculator.sub(3, 8), -5)
        self.assertEqual(calculator.sub(5, 5), 0)

    def test_mul(self):
        calculator = Calculator()
        self.assertEqual(calculator.mul(8, 3), 24)
        self.assertEqual(calculator.mul(5, 0), 0)
        self.assertEqual(calculator.mul(-4, 3), -12)
        self.assertEqual(calculator.mul(-2, -3), 6)

    def test_div(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(8, 2), 4.0)
        self.assertEqual(calculator.div(9, 3), 3.0)
        self.assertEqual(calculator.div(5, 2), 2.5)
        self.assertEqual(calculator.div(-8, 2), -4.0)

    def test_div_by_zero(self):
        calculator = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.div(8, 0)

    def test_factorize(self):
        calculator = Calculator()
        self.assertEqual(calculator.factorize(8), [2, 2, 2])
        self.assertEqual(calculator.factorize(12), [2, 2, 3])
        self.assertEqual(calculator.factorize(27), [3, 3, 3])
        self.assertEqual(calculator.factorize(13), [13])
        self.assertEqual(calculator.factorize(1), [])

    def test_add_english_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("three", "1.600"), 4.6)
        self.assertEqual(calculator.add("two", "five"), 7)
        self.assertEqual(calculator.add("  eight  ", "2"), 10)

    def test_add_spanish_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("cinco", "siete"), 12)
        self.assertEqual(calculator.add("uno", "dos"), 3)
        self.assertEqual(calculator.add("ocho", "nueve"), 17)

    def test_add_russian_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("семь", "восемь"), 15)
        self.assertEqual(calculator.add("один", "два"), 3)
        self.assertEqual(calculator.add("три", "пять"), 8)

        
    def test_add_roman_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("III", "VIII"), 11)
        self.assertEqual(calculator.add("0", "X"), 10)
        self.assertEqual(calculator.add("IV", "VI"), 10)

    def test_add_chinese_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("三", "五"), 8)
        self.assertEqual(calculator.add("一", "九"), 10)

    def test_multilingual_operations(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("ocho", "nueve"), 17)
        self.assertEqual(calculator.sub("ocho", "nueve"), -1)
        self.assertEqual(calculator.mul("ocho", "nueve"), 72)
        self.assertEqual(calculator.div("ocho", "dos"), 4.0)

    def test_multilingual_factorize(self):
        calculator = Calculator()
        self.assertEqual(calculator.factorize("три"), [3])
        self.assertEqual(calculator.factorize("X"), [2, 5])
        self.assertEqual(calculator.factorize("ocho"), [2, 2, 2])
        self.assertEqual(calculator.factorize(27), [3, 3, 3])
        self.assertEqual(
            calculator.factorize(1092),
            [2, 2, 3, 7, 13]
        )
        self.assertEqual(
            calculator.factorize(32768),
            [2] * 15
        )
        self.assertEqual(
            calculator.factorize(10952347),
            [7, 23, 59, 1153]
        )
        self.assertEqual(
            calculator.factorize(100000039),
            [100000039]
        )

    def test_invalid_factorize(self):
        calculator = Calculator()
        with self.assertRaises(ValueError):
            calculator.factorize(0)
        with self.assertRaises(ValueError):
            calculator.factorize(2.5)


if __name__ == "__main__":
    unittest.main()
