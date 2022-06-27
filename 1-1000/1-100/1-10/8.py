c2n = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = False
        ans = 0

        digit_started = False
        idx = 0
        while idx < len(s):
            if s[idx] in c2n:
                digit_started = True
                ans = 10 * ans + c2n[s[idx]]

            elif s[idx] in [" ", "-", "+"]:
                if digit_started:
                    break
                if s[idx] == "-":
                    is_negative = True
                if s[idx] != " ":
                    digit_started = True
            else:
                break

            idx += 1

        if is_negative:
            ans = -ans

        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648

        return ans
