import unittest
from skeleton import *

class TestFizzBuzz(unittest.TestCase):

    def __init__(self, solution):
        self.solution = solution

    def test_fizz_buzz(self):
        
        self.assertRaises(TypeError, self.solution(), None)
        self.assertRaises(ValueError, self.solution(), 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
