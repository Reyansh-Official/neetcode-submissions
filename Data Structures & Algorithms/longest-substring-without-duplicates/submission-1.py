class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 

        if len(s) == 1:
            return 1 

        l, r = 0, 1 
        unique_set = set()
        unique_set.add(s[l]) 
        result = 1 

        while r < len(s):
            if s[r] not in unique_set:
                unique_set.add(s[r]) 
                result = max(result, (r - l) + 1) 
                r += 1 
                
            else:
                unique_set.discard(s[l])
                l += 1 
                
        return result 
            
        