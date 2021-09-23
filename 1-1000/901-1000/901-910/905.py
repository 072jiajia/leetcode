class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        EvenList = []
        OddList = []
        for number in nums:
            if number & 1:
                OddList.append(number)
            else:
                EvenList.append(number)
        return EvenList + OddList
