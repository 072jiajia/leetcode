class Solution:
    def check_all_1(self, nums):
        for num in nums:
            if num != 1:
                return False
        return True
    def longestSubarray(self, nums: List[int]) -> int:
        if self.check_all_1(nums):
            return len(nums) - 1

        max_consecutive = 0
        last_consecutive = 0
        consecutive = 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                max_consecutive = max(max_consecutive, consecutive + last_consecutive)
                last_consecutive = consecutive
                consecutive = 0
        max_consecutive = max(max_consecutive, consecutive + last_consecutive)
        return max_consecutive
