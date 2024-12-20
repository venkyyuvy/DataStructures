# lc 1
# Two sum problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List
import pytest

pytest.problem_name = "two_sum"
pytest.method_name = "twoSum"


def test_two_sum(solution):
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution([3, 2, 4], 6) == [1, 2]
    assert solution([3, 3], 6) == [0, 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict([(val, ix) for ix, val in enumerate(nums)])
        for ix, num in enumerate(nums):
            counter_index = hashmap.get(target - num, -1)
            if counter_index not in [-1, ix]:
                return [ix, counter_index]

    def twoSum_o(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ix, num in enumerate(nums):
            counter_index = hashmap.get(target - num, -1)
            if counter_index != -1:
                return [ix, counter_index]
            else:
                hashmap[num] = ix

    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:
        for ix, num in enumerate(nums):
            for iy, counter in enumerate(nums[ix + 1:], ix + 1):
                if num + counter == target:
                    return [ix, iy]


#
# def test_twoSum():
#     assert Solution().twoSum_o([2, 7, 11, 15], 9) == [0, 1]
#     assert Solution().twoSum_bf([2, 7, 11, 15], 9) == [0, 1]
#     assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
