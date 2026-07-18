class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)  
        s1_count = [0] * 26
        window_count = [0] * 26 

        for char in s1:
            index = ord(char) - ord('a') 
            s1_count[index] += 1 
        
        for right in range(len(s2)):
            # Add the newest character
            index = ord(s2[right]) - ord("a")
            window_count[index] += 1

            # Remove the character that is now outside the window
            if right >= window_size:
                left_index = ord(s2[right - window_size]) - ord("a")
                window_count[left_index] -= 1

            if window_count == s1_count:
                return True

        return False  

