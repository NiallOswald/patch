import unittest, skeleton


class TestCase(unittest.TestCase):

    def test_two_sum(self):
        solution = skeleton.Solution()
        self.assertRaises(TypeError, solution.two_sum, None, None)
        self.assertRaises(ValueError, solution.two_sum, [], 0)
        target = 6
        nums = [3, 3, 4, 5]
        expected = [0, 1]
        self.assertEqual(solution.two_sum(nums, target), expected)
        print("Success: test_two_sum")


def main():
    test = TestCase()
    test.test_two_sum()


if __name__ == "__main__":
    main()
