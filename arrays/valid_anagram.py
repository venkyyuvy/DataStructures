# lc 217
# contains duplicate
# sort and look at the neighbor
# hash / set to store the seen ones

from collections import defaultdict
import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = [
    "isAnagram",
]


def test_duplicate(solutions):
    for sol in solutions:
        assert sol("dog", "god") is True
        assert sol("pen", "") is False
        assert sol("powder", "podwre") is True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for s_i in s:
            chars[s_i] += 1
        for t_i in t:
            if count := chars.get(t_i, -1):
                if count < 1:
                    return False
                chars[t_i] -= 1
        return sum(chars.values()) == 0
