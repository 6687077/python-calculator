import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add method
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-10, -5), -15)

    # Test cases for subtract method
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    # Test cases for multiply method
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    # Test cases for divide method
    def test_divide_exact_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_remainder(self):
        self.assertEqual(self.calc.divide(9, 2), 4)  # Should return quotient

    # Test cases for modulo method
    def test_modulo_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

if __name__ == '__main__':
    unittest.main()
