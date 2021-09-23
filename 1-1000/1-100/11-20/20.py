class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None]
        for c in s:
            if c == '(':
                stack.append(1)
            elif c == '[':
                stack.append(2)
            elif c == '{':
                stack.append(3)
            elif c == ')':
                if stack.pop(-1) != 1:
                    return False
            elif c == ']':
                if stack.pop(-1) != 2:
                    return False
            else:
                if stack.pop(-1) != 3:
                    return False
        return len(stack) == 1
