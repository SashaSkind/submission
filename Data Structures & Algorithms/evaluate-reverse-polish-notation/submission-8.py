class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [tokens[0]]
        for token in tokens[1:]:
            if token == "+" or  token == "-" or token == "*" or token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "/":
                    stack.append(str(int(eval(f"{num1} / {num2}"))))
                else:
                    string = num1 + token + num2
                    stack.append(str(eval(string)))
            else:
                stack.append(token)
        return int(stack[-1])
            
        