class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        product_array = []

        while i < n: 
            product = 1
            j = 0

            while j < n:
                if i != j:
                    product *= nums[j] 
                j += 1
            
        
            product_array.append(product) 
            i +=1
        
        return product_array 



        
        