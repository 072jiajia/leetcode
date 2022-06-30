from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num == val:
                continue
            nums[idx] = num
            idx += 1
        return idx
