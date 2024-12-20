# lc 49
# group anagram

from typing import List
from collections import defaultdict
import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = [
    "groupAnagrams",
]

def sort_anagrams(output):
    for groups in output:
        groups.sort()
    return sorted(output)


def test_duplicate(solutions):
    for sol in solutions:
        assert sort_anagrams(sol(["eat","tea","tan","ate","nat","bat"])) == sort_anagrams([["bat"],["nat","tan"],["ate","eat","tea"]])
        assert sol([""]) == [[""]]
        assert sol(["a"]) == [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            char_counters = [0]*26
            for char in string:
                char_counters[ord(char) - ord('a')] += 1
            hash_map[tuple(char_counters)].append(string)
        return list(hash_map.values())


