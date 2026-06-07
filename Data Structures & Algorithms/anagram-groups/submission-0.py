class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dictionary = {} 
        for word in strs: 
            sorted_word = sorted(word)
            join_sorted = "".join(sorted_word) 

            if join_sorted in group_dictionary:
                group_dictionary[join_sorted].append(word)
            else:
                group_dictionary[join_sorted] = [word]    

        
        return list(group_dictionary.values()) 

    