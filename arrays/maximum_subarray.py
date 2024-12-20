# lc 53
# finding the contiguous subarray with maximum sum

from typing import List

import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = ["maxSubArray", "kadane_dp"]


def test_duplicate(solutions):
    for sol in solutions:
        assert sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert sol([5, 4, -1, 7, 8]) == 23


class Solution:
    def kadane_dp(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global

    def maxSubArray(self, nums: List[int]) -> int:
        max_ = -float("inf")
        for ix, num in enumerate(nums):
            for iy, val in enumerate(nums[ix:], ix):
                max_ = max(max_, sum(nums[ix: iy + 1]))
        return max_ if max_ != -float("inf") else -1
