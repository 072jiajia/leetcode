class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumPos = {}
        for i in range(len(nums)):
            if target - nums[i] in NumPos:
                return NumPos[target - nums[i]], i
            NumPos[nums[i]] = i
