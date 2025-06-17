class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]
if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "6", "*"])) 
    print(s.evalRPN(["4", "24", "3", "/", "+"])) 