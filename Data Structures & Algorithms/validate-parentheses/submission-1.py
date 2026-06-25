class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')':'(', ']':'[', '}':'{'}  
        for char in s:
            if char in match: 
                top_element = stack.pop() if stack else '#' 
                if match[char] != top_element:
                    return False
            else:
                stack.append(char)       
        
        return not stack
        


        