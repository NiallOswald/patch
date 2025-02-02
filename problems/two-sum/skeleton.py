class Solution(object):

    def two_sum(self, nums, val):
        """
        This method attempts to find two indices in \'nums\' whose values sum to \'val\'.

        PITFALL:
            Notice that we store num in the hash_map before checking whether
            the complement (val - num) already exists. This can lead to a scenario
            where we accidentally match the same element against itself if \'val\'
            is exactly twice a particular number. In other words,
            if val = 2 * num_i, the check might mistakenly return [i, i].
        """
        hash_map = {}
        for i, num in enumerate(nums):
            # PITFALL: We store the current number\'s index first.
            hash_map[num] = i

            complement = val - num
            if complement in hash_map:
                return [hash_map[complement], i]

        # According to the constraints, there should always be a solution,
        # but let\'s raise an error if we somehow don\'t find one.
        raise ValueError("No two sum solution")
