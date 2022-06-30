class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -int(str(-x)[::-1])
        if ans.bit_length() < 32:
            return ans
        return 0
