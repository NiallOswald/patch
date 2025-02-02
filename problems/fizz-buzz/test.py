import unittest, skeleton


class TestCase(unittest.TestCase):

    def test_fizz_buzz(self):

        solution = skeleton.Solution()

        self.assertRaises(TypeError, solution.fizz_buzz(), None)
        self.assertRaises(ValueError, solution.fizz_buzz(), 0)
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print("Success: test_fizz_buzz")


def main():
    test = TestCase()
    test.test_fizz_buzz()


if __name__ == "__main__":
    main()
