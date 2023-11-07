from typing import List
from functools import lru_cache


class Solution:
    def rob_memoization(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache
        def rob_helper(i):
            if i >= n:
                return 0

            return max(nums[i] + rob_helper(i+2),
                       rob_helper(i+1))
        return rob_helper(0)

    def rob_iterative(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(*nums)
        rob_amt = [0] * (n+1)
        rob_amt[0] = nums[0]
        rob_amt[1] = max(nums[:2])
        for i in range(2, n):
            rob_amt[i] = max(nums[i] + rob_amt[i - 2], rob_amt[i - 1])

        return rob_amt[n-1]

    def rob_space_optimized(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(*nums)
        base1 = nums[0]
        base2 = max(nums[:2])
        for i in range(2, n):
            rob_amt = max(nums[i] + base1, base2)
            base1, base2 = base2, rob_amt

        return rob_amt

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        base2 = nums[-1]
        base1 = 0
        rob_amt = base2
        for i in reversed(range(0, n - 1)):
            rob_amt = max(nums[i] + base1, base2)
            base1, base2 = base2, rob_amt
        return rob_amt
