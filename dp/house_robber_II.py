from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def helper(start, end):
            base1 = 0
            base2 = nums[end]
            rob_amt = base2
            for i in reversed(range(start, end)):
                rob_amt = max(nums[i] + base1, base2)
                base1, base2 = base2, rob_amt
            return rob_amt
    
        return max(helper(0, n-2), helper(1, n-1))


class NeetCodeSolution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
