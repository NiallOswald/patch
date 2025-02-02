class Subsequence(object):

    def longest_inc_subseq(self, seq):
        """
        Returns an array representing one of the longest increasing subsequences
        from the list \'seq\'. Contains an intentional bug where duplicates are
        allowed to continue the increasing sequence (using <= instead of <).
        """

        # Basic validation: if seq is None or empty, return empty list
        if not seq:
            return []

        # Optional: further validation to ensure all elements are integers
        for val in seq:
            if not isinstance(val, int):
                # Let\'s just return empty if invalid
                return []

        # dp[i] will hold the length of the LIS ending at index i
        dp = [1] * len(seq)

        # prev[i] will hold the index of the predecessor of i in the LIS
        prev = [-1] * len(seq)

        # Variables to track the maximum length and the index where it occurs
        max_len = 1
        max_index = 0

        # Fill dp using the LIS definition
        for i in range(len(seq)):
            for j in range(i):
                # --------------------------------------------------------------
                # PITFALL: Using <= here means this code treats duplicates
                # as "increasing." The standard strict check should be <.
                # --------------------------------------------------------------
                if seq[j] <= seq[i]:  # <-- Bug: should be seq[j] < seq[i]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # Reconstruct the longest increasing subsequence
        lis = []
        curr = max_index
        while curr != -1:
            lis.append(seq[curr])
            curr = prev[curr]

        # The subsequence is built backwards, so reverse it
        lis.reverse()

        return lis
