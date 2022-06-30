class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        stride = 2 * (numRows - 1)
        ans = [s[0::stride]]

        for offset1 in range(1, numRows-1):
            offset2 = 2 * numRows - 2 - offset1
            while True:
                if offset1 < len(s):
                    ans.append(s[offset1])
                    offset1 += stride
                else:
                    break

                if offset2 < len(s):
                    ans.append(s[offset2])
                    offset2 += stride
                else:
                    break

        ans.append(s[numRows-1::stride])

        return "".join(ans)
