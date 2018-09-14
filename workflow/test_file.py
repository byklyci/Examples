import unittest

def average(values=None):
    """Computes the arithmetic mean of a list of numbers.

        >>> print(average([20, 30, 70]))
        40.0
        >>> print(average([10,10,10]))
        10.0
        """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())

def sum_val(values):
    return sum(values)

def just_w(value):
    return value


class TestAverage(unittest.TestCase):
    def setUp(self):
        self.result = average([20, 40, 60])
        self.r = sum_val([20, 40, 60])
        self.wr = just_w(str)

    def tearDown(self):
        self.result.is_integer()

    def test_average(self):
        self.assertEqual(self.result, 40.0)

    def test_sum(self):
        self.assertEqual(self.r, 120)

    def test_write(self):
        self.assertEqual(self.wr, str)

if __name__ == '__main__':
    unittest.main()


