Value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        SUM = 0
        Last = 0
        for index in range(len(s)-1, -1, -1):
            v = Value[s[index]]
            if v >= Last:
                SUM += v
            else:
                SUM -= v
            Last = v
        return SUM
