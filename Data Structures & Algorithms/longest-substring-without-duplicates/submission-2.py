class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique_set = set()
        result = 0

        for r in range(len(s)):
            while s[r] in unique_set:
                unique_set.discard(s[l]) 
                l += 1 
            
            unique_set.add(s[r])
            result = max(result, (r - l) + 1)
        
        return result 

            
            
        