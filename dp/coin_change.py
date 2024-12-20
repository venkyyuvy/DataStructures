from typing import List
import math


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        # dp rows - coins; coins are the amounts
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for amt in range(1, amount+1):
                if coins[i-1] <= amt:
                    dp[i][amt] = (dp[i][amt - coins[i-1]]) + \
                                     dp[i-1][amt]
                else:
                    dp[i][amt] = dp[i-1][amt]
        return dp[n][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        # dp rows - coins; coins are the amounts
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(amount + 1):
            dp[0][i] = math.inf

        for i in range(1, n+1):
            for amt in range(1, amount+1):
                if coins[i-1] <= amt:
                    dp[i][amt] = min(dp[i][amt - coins[i-1]] + 1,
                                     dp[i-1][amt])
                else:
                    dp[i][amt] = dp[i-1][amt]
        if dp[n][amount] == math.inf:
            return -1
        return dp[n][amount]
