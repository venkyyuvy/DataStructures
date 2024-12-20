# lc 121
# best time buy and sell the stock
from typing import List


class Solution:
    def maxProfit_opt(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        min_price = float("inf")
        max_profit = 0
        for sell_price in prices:
            max_profit = max(max_profit, sell_price - min_price)
            min_price = min(min_price, sell_price)
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        max_prices = [prices[-1]]
        for price in reversed(prices):
            max_prices.append(max(max_prices[-1], price))
        max_prices = list(reversed(max_prices))
        max_profit = 0
        for day, buy_price in enumerate(prices):
            max_profit = max(max_profit, max_prices[day + 1] - buy_price)
        return max_profit


def test_max_profit():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit_opt([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit_opt([7, 6, 4, 3, 1]) == 0
