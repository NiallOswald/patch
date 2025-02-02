

class Solution(object):

    def move_zeroes(self, nums):
        # Edge case: Handle invalid or empty input
        if not isinstance(nums, list):
            print("Invalid input: \'nums\' must be a list.")
            return  # Early exit

        if not nums:  # Empty list, do nothing
            return

        # Two-pointer approach
        j = 0  # j is where the next non-zero element will go
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fills the remainder with zeroes
        # PITFALL: We use "< len(nums) - 1" instead of "< len(nums)"
        # This means if j == len(nums) - 1 after the loop, the last element
        # might not be set to 0 properly, leaving a stray value.
        while j < len(nums) - 1:
            nums[j] = 0
            j += 1

        # Intentionally missing the final 0 assignment if j == len(nums) - 1


