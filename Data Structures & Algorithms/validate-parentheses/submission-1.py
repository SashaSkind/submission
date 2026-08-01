class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for s in s:
            if s == "(" or s == "{" or s == "[":
                stack.append(s) 
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if (s == ")" and tmp != "(") or (s == "}" and tmp != "{") or (s == "]" and tmp != "["):
                    return False


        return len(stack) == 0
        