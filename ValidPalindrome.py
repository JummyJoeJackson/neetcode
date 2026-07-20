class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""

        for c in s:
            if c.isalnum():
                copy += c
        
        copy = copy.lower()

        for i in range(len(copy)//2):
            if copy[i] != copy[-1-i]:
                return False
        
        return True
