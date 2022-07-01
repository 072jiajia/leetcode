class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s.lower():
            ASCII = ord(c)
            if 97 <= ASCII and ASCII <= 122:
                string += c
            if 48 <= ASCII and ASCII <= 57:
                string += c
        return string == string[::-1]
