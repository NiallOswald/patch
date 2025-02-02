import unittest, skeleton


class TestCase(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = skeleton.CoinChanger()
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 5)
        self.assertEqual(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print("Success: test_coin_change")


def main():
    test = TestCase()
    test.test_coin_change()


if __name__ == "__main__":
    main()
