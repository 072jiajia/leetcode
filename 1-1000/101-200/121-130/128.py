class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        MaxCount = 0
        for num in nums:
            if num not in NumSet:
                continue

            NumSet.remove(num)
            right = num + 1
            left = num - 1
            while right in NumSet:
                NumSet.remove(right)
                right += 1

            while left in NumSet:
                NumSet.remove(left)
                left -= 1

            MaxCount = max(MaxCount, right - left - 1)

        return MaxCount
