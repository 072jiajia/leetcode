from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        idx = 0
        for num in nums:
            if num == last:
                continue
            last = num
            nums[idx] = num
            idx += 1
        return idx
