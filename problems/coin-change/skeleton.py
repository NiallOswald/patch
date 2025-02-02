

class CoinChanger(object):

    def make_change(self, coins, total):
        """
        Returns the number of unique ways to make `total` cents
        from the given list of coin denominations.
        
        There is a subtle pitfall in the way the DP array is updated—
        watch out for how we iterate over amounts vs. coins. This
        can inadvertently lead to double-counting certain combinations.
        """
        # dp[i] will store the number of ways to make i cents.
        dp = [0] * (total + 1)
        dp[0] = 1  # Base case: There\'s 1 way to make 0 cents (use no coins).

        # PITFALL: Iterating amounts first and then looping through coins
        # can accidentally count some combinations multiple times.
        for amt in range(1, total + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] += dp[amt - coin]

        return dp[total]


