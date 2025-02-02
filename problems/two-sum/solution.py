class Solution(object):

    def two_sum(self, nums, val):
        if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums) or not isinstance(val, int):
            raise TypeError("nums must be a list of integers")
        if not nums:
            raise ValueError("nums cannot be an empty list")

        seen = {}
        for i, num in enumerate(nums):
            complement = val - num
            if complement in seen:
                return [seen[complement], i]  # Return indices immediately
            if num not in seen:  # Ensure first occurrence is stored
                seen[num] = i  

        return []  # Should never reach here due to constraints
