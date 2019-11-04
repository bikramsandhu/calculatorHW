import unittest
from Calculator import Calculator
from CSVReader import CSVReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(self.calculator.result, 0)

    def test_addition(self):
        test_data = CSVReader("Tests/Data/addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CSVReader("Tests/Data/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CSVReader("Tests/Data/multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value1'], row['Value2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CSVReader("Tests/Data/division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value1'], row['Value2']), result)
            self.assertEqual(self.calculator.divide.result, result)

    def test_square(self):
        test_data = CSVReader("Tests/Data/square.csv")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value1']), result)
            self.assertEqual(self.calculator.square.result, result)

    def test_squareroot(self):
        test_data = CSVReader("Tests/Data/squareroot.csv")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value1']), result)
            self.assertEqual(self.calculator.squareroot.result, result)

    def test_results_property(self):

        calculator.add(2, 1)
        self.assertEqual(self.calculator.result, 3)



if __name__ == '__main__':
    unittest.main()
