class Solution(object):

    def fizz_buzz(self, num):
        # If the input is not an integer or is less than 1,
        # return an empty list (simple invalid input handling).
        if not isinstance(num, int) or num < 1:
            return []

        result = []
        for i in range(1, num + 1):
            # PITFALL: The check for "FizzBuzz" is done last,
            # so if i is divisible by 3, the code will never
            # get down to check "elif i % 3 == 0 and i % 5 == 0".
            if i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                # This condition never actually triggers,
                # because the \'if i % 3 == 0\' above
                # has already caught multiples of 3.
                result.append("FizzBuzz")
            else:
                result.append(str(i))

        return result
