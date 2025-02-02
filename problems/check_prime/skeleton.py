import math


class Math(object):

    def check_prime(self, num):
        # 1) Handle invalid input: must be an integer
        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")

        # 2) By definition, numbers less than 2 (including 1) are not prime
        if num < 2:
            return False

        # 3) Check divisibility from 2 up to the square root of the number
        #    Common Pitfall: forgetting to include the upper bound properly
        for i in range(2, int(math.sqrt(num))):  # <-- Potential logical issue here
            if num % i == 0:
                return False

        # If no divisors were found, the number is prime
        return True
