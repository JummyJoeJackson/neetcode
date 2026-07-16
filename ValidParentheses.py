class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(","{","["]
        close = [")","}","]"]

        for c in s:
            if c in open:
                stack.append(c)
            elif c in close:
                if len(stack) == 0 or open.index(stack[-1]) != close.index(c):
                    return False
                stack.pop()

        return len(stack) == 0
