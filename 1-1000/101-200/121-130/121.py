from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 1000000
        best = 0
        for price in prices:
            if price < low:
                low = price
            else:
                best = max(best, price - low)

        return best
