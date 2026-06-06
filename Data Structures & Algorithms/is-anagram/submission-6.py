class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sLower = s.lower() 
        tLower = t.lower() 

        if len(sLower) != len(tLower): 
            return False

        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1 
        
        for ch in t:
            if ch in seen: 
                seen[ch] -= 1 
                if seen[ch] < 0:
                    return False 
            else:
                return False
        
        return True


              
