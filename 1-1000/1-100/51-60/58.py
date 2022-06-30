class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s)-1
        while s[idx] == " ":
            idx -= 1
        idx2 = idx
        while s[idx2] != " ":
            idx2 -= 1
            if idx2 < 0:
                break

        return idx - idx2
