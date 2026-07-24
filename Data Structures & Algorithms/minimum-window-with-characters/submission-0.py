class Solution:
    def minWindow(self, s: str, t: str) -> str:

        result_start = 0
        result_length = float("inf") 
        l = 0  
        t_dict = {}
        freq_dict = {} 

        for char in t: 
            t_dict[char] = 1 + t_dict.get(char, 0)  

        need = len(t_dict)
        have = 0
        
        for r in range(len(s)):
            freq_dict[s[r]]  = 1 + freq_dict.get(s[r], 0) 

            if s[r] in t_dict and freq_dict[s[r]] == t_dict[s[r]]: 
                have += 1   
            
            while have == need:
                window_length = r - l + 1 
                left_char = s[l]  

                if window_length < result_length:
                    result_length = window_length 
                    result_start = l
                    
                
                freq_dict[left_char] -= 1 

                if left_char in t_dict and freq_dict[left_char] < t_dict[left_char]:
                    have -= 1 
                
                l += 1 

        if result_length == float("inf"):
            return "" 

        return s[result_start:result_start + result_length]
                

    




        
        