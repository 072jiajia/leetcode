class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c = ""
        take = 0
        for i in range(max(len(a), len(b))):
            _a = 1 if i < len(a) and a[i] == '1' else 0
            _b = 1 if i < len(b) and b[i] == '1' else 0
            s = take + _a + _b
            if s >= 2:
                s -= 2
                take = 1
            else:
                take = 0

            if s == 1:
                c += "1"
            else:
                c += "0"
        if take == 1:
            c += "1"
        return c[::-1]


print(Solution().addBinary('11', '1'))
print(Solution().addBinary('1010', '1011'))
