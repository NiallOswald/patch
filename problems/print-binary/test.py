import unittest, skeleton


class TestCase(unittest.TestCase):

    def test_print_binary(self):
        bit = skeleton.Bits()
        self.assertEqual(bit.print_binary(None), "ERROR")
        self.assertEqual(bit.print_binary(0), "ERROR")
        self.assertEqual(bit.print_binary(1), "ERROR")
        num = 0.625
        expected = "0.101"
        self.assertEqual(bit.print_binary(num), expected)
        num = 0.987654321
        self.assertEqual(bit.print_binary(num), "ERROR")
        print("Success: test_print_binary")


def main():
    test = TestCase()
    test.test_print_binary()


if __name__ == "__main__":
    main()
