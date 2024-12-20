from typing import List
from functools import lru_cache
class Solution:
    def wordBreak_recrusive(self, s: str, wordDict: List[str]) -> bool:
        """
        split at i if word is present and recurse
        
        """
        @lru_cache
        def wordBreakHelper(string):            
            if not string:
                return True
            current_word = ''
            for ix, i in enumerate(string):
                current_word += i
                if current_word in word_dict and wordBreakHelper(string[ix+1:]):
                    return True
            return False
                
        word_dict = set([])
        for word in wordDict:
            word_dict.add(word)
            
        return wordBreakHelper(s)
            
    def wordBreak_recrusive(self, s: str, wordDict: List[str]) -> bool:
        """
        split at i if word is present and recurse
        
        """     
        word_dict = set(wordDict)
        
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in reversed(range(n)):
            for j in range(i+1, n+1):
                if dp[j] and s[i:j] in word_dict:
                    dp[i] = True
                    break
        return dp[0]
