class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(","{","["]
        close = [")","}","]"]

        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif s[i] in close:
                if len(stack) == 0 or open.index(stack[-1]) != close.index(s[i]):
                    return False
                stack.pop()

        return len(stack) == 0
