from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            lefth = height[left]
            righth = height[right]

            if lefth < righth:
                ans = max(lefth * (right - left), ans)
                left += 1
            else:
                ans = max(righth * (right - left), ans)
                right -= 1

        return ans
