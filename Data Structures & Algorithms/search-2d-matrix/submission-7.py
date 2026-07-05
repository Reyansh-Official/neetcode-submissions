class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):


            if matrix[i][-1] < target:
                continue 

            elif target < matrix[i][0]:
                return False

            else: 
                low = 0 
                high = len(matrix[i]) - 1 

                while low <= high:
                    mid = (low + high) // 2 

                    if matrix[i][mid] < target:
                        low = mid + 1 
                    
                    elif matrix[i][mid] > target:
                        high = mid - 1 
                    
                    else:
                        return True  

                return False  

        return False 


