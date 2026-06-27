class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                second_element = stack.pop()
                first_element = stack.pop()

                if token == "+":
                    stack.append(first_element + second_element)
                elif token == "-":
                    stack.append(first_element - second_element)
                elif token == "*":
                    stack.append(first_element * second_element)
                else:
                    stack.append(int(first_element / second_element))          
        
        return stack[0] 


                

                    

            
        