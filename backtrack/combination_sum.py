from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def generate(prefix, sum_):
            if sum_ > target:
                return
            if sum_ == target:
                ans.append(prefix)
                return
                
            for candidate in candidates:
                if not prefix:
                    generate(prefix + [candidate], sum_ + candidate)
                elif candidate >= prefix[-1]:
                    generate(prefix + [candidate], sum_ + candidate)
                
        generate([], 0)
        return list(ans)
        
