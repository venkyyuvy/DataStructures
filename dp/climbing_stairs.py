from functools import lru_cache
# class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n ==0 or n==1:
            return 1
        return self.climbStairs(n-2) + self.climbStairs(n-1)

    # iterative approach
    def climbStairs_iter(self, n: int) -> int:
        ways = [None] * (n + 1)
        ways[0] = ways[1] = 1
        for i in range(2, n+1):
            ways[i] = ways[i-2] + ways[i-1]
        return ways[n]
        
    # optimized iterative approach
    def climbStairs_optimized_iter(self, n: int) -> int:
        if n == 0 or n==1:
            return 1
        ways_2_back = ways_1_back = 1
        for i in range(2, n+1):
            ways = ways_2_back + ways_1_back
            ways_2_back, ways_1_back = ways_1_back, ways
        return ways
