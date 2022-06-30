from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        left = 0
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
