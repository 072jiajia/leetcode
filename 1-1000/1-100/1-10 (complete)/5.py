class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        # odd
        for i in range(len(s)):
            length = 1
            while i - length >= 0 and i+length < len(s):
                if s[i-length] == s[i+length]:
                    length += 1
                else:
                    break
            length -= 1

            if length * 2 + 1 > len(ans):
                ans = s[i-length:i+length+1]

        # even
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                continue

            length = 1
            while i - length >= 0 and i+1+length < len(s):
                if s[i-length] == s[i+1+length]:
                    length += 1
                else:
                    break
            length -= 1

            if length * 2 + 2 > len(ans):
                ans = s[i-length:i+length+2]

        return ans
