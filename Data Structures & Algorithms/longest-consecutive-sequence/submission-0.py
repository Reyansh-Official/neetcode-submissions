class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        longest = 0

        for num in nums_set:
            if (num - 1) not in nums_set: 
                next_val = 0 

                while (num + next_val) in nums_set:
                    next_val += 1
                
                longest = max(next_val, longest)     

        return longest 
        