import unittest

from Calculator.Calculator import Calculator
from CsvReader.CSVReader import CSVReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)



if __name__ == '__main__':
    unittest.main()
