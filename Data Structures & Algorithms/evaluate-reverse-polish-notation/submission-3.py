class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        num_1 = 0
        num_2 = 0

        for t in tokens:
            if t in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()

                if t == "+":
                    stack.append(num_1+num_2)
                elif t == "-":
                    stack.append(num_1-num_2)
                elif t == "*":
                    stack.append(num_1*num_2)
                elif t == "/":
                    stack.append(int(num_1/num_2))
            else:
                stack.append(int(t))
        
        return stack[0]



