class Solution:

    def encode(self, strs: List[str]) -> str:
        final_encoded = ""
        for word in strs: 
            word_length = len(word) 
            final_encoded += str(word_length) + ":" + word  
        
        return final_encoded 


    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != ":":
                j += 1 

            length =int(str(s[i:j]))
            result.append(s[j + 1: j + 1 + length]) 
            i = j + 1 + length
        

        return result
