import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.result, 0)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiplication(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.result, 6)

    def test_division(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.result, 3)

    def test_square(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_squareroot(self):
        calculator = Calculator()
        self.assertEqual(calculator.squareroot(9), 3)
        self.assertEqual(calculator.result, 3)

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(2, 1)
        self.assertEqual(calculator.result, 3)



if __name__ == '__main__':
    unittest.main()
