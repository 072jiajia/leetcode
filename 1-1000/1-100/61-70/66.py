from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits)-1
        while True:
            digits[idx] += 1
            if digits[idx] == 10:
                digits[idx] = 0
                if idx == 0:
                    digits = [1] + digits
                    return digits
            else:
                break
            idx -= 1
        return digits
