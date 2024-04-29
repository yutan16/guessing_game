import unittest
import guessingGame


class GGameTest(unittest.TestCase):
    def guessingGameTest_FirstGreaterThanLast(self):
        param_num1 = 10
        param_num2 = 1
        result = guessingGame(param_num1, param_num2)
        self.assertEqual(
            result, 'RANGE ERROR: First input is greater than the last input. Please restart.')
