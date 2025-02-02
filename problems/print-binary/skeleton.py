

class Bits(object):

    def print_binary(self, num):
        """
        Converts a floating-point number 0 < num < 1 into its binary representation:
        1) If num is not in (0, 1), returns "ERROR"
        2) Otherwise, returns "0." followed by the bits of num in binary
        3) If the length of the representation would exceed 32, returns "ERROR"
        """
        if num <= 0 or num >= 1:
            return "ERROR"  # Out of expected range
        
        # Start with the leading characters "0."
        result = "0."
        
        # Generate up to 32 bits (attempting to stay within 32 chars total).
        # -- PITFALL WARNING: There\'s a subtle issue here that can
        #    cause the output to exceed the 32-character limit in some cases.
        for _ in range(32):
            num *= 2
            if num >= 1:
                result += "1"
                num -= 1
            else:
                result += "0"
            
            # If the fractional part has become zero, we are done
            if num == 0:
                break

        # If we\'ve used up our 32 potential bits but the number isn\'t fully
        # converted, we intend to return "ERROR"
        if num != 0:
            return "ERROR"
        
        return result

