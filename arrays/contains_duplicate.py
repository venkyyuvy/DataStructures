# lc 217
# contains duplicate
# sort and look at the neighbor
# hash / set to store the seen ones

from typing import List

import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = [
    "containsDuplicate_set",
    "containsDuplicate_sort",
    "containsDuplicate",
]


def test_duplicate(solutions):
    for sol in solutions:
        assert sol([1, 2, 3, 1]) is True
        assert sol([1, 2, 3, 4]) is False


class Solution:
    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for ix in range(len(nums) - 1):
            if nums[ix] == nums[ix + 1]:
                return True
        return False

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set(nums)
        return len(hash) != len(nums)
