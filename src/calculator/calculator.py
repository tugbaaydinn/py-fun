
def convert_number(value):
    if not isinstance(value, str):
        return value

    value = value.strip().lower()

    numbers = {
        # English
        "zero": 0, "one": 1, "two": 2,
        "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8,
        "nine": 9, "ten": 10,

        # Spanish
        "cero": 0, "uno": 1, "dos": 2,
        "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8,
        "nueve": 9, "diez": 10,

        # Russian
        "ноль": 0, "один": 1, "два": 2,
        "три": 3, "четыре": 4, "пять": 5,
        "шесть": 6, "семь": 7,
        "восемь": 8, "девять": 9,
        "десять": 10,

        # Chinese
        "零": 0, "一": 1, "二": 2,
        "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8,
        "九": 9, "十": 10
    }

    if value in numbers:
        return numbers[value]

    # Roman numerals
    roman_values = {
        "i": 1, "v": 5, "x": 10,
        "l": 50, "c": 100,
        "d": 500, "m": 1000
    }

    if value and all(char in roman_values for char in value):
        total = 0
        previous = 0

        for char in reversed(value):
            current = roman_values[char]

            if current < previous:
                total -= current
            else:
                total += current

            previous = current

        return total

    # Numeric strings
    try:
        return int(value)
    except ValueError:
        return float(value)


class Calculator(object):
    _instance = None

    def add(_self, a, b):
        return convert_number(a) + convert_number(b)

    def sub(_self, a, b):
        return convert_number(a) - convert_number(b)

    def mul(_self, a, b):
        return convert_number(a) * convert_number(b)

    def div(_self, a, b):
        return convert_number(a) / convert_number(b)

    def factorize(_self, n):
        n = convert_number(n)

        if not isinstance(n, int) or isinstance(n, bool):
            raise ValueError("Factorization requires an integer")

        if n < 1:
            raise ValueError("Factorization requires a positive integer")

        factors = []
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor

            divisor += 1

        if n > 1:
            factors.append(n)

        return factors

    def __init__(self):
        pass