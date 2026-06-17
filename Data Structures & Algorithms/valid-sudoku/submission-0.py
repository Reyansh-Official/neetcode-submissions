class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_values = [set() for i in range(9)]
        col_values = [set() for i in range(9)]
        box_values = [set() for i in range(9)] 

        for r in range(9):
            for c in range(9): 

                val = board[r][c]

                if val == ".":
                    continue 
                
                box_index = (r // 3) * 3 + (c // 3) 

                if (val in row_values[r] or
                    val in col_values[c] or
                    val in box_values[box_index]):

                    return False
                
                row_values[r].add(val) 
                col_values[c].add(val)
                box_values[box_index].add(val) 

        return True
        