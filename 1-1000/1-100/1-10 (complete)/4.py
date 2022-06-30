class Solution:
    def find_index(self, nums1, nums2, st1, st2, index):
        if index == 0:
            if len(nums1) == st1:
                return nums2[st2]
            if len(nums2) == st2:
                return nums1[st1]
            return min(nums1[st1], nums2[st2])
        
        half = (index-1) >> 1
        index1 = st1 + half
        index2 = st2 + half
        if index1 >= len(nums1):
            return self.find_index(nums1, nums2, st1, index2+1, index - half-1)
        elif index2 >= len(nums2):
            return self.find_index(nums1, nums2, index1+1, st2, index - half-1)
        elif nums1[index1] > nums2[index2]:
            return self.find_index(nums1, nums2, st1, index2+1, index - half-1)
        else:
            return self.find_index(nums1, nums2, index1+1, st2, index - half-1)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums = len(nums1) + len(nums2)
        if len_nums % 2 == 0:
            return (self.find_index(nums1, nums2, 0, 0, len_nums // 2) + self.find_index(nums1, nums2, 0, 0, (len_nums-1) // 2)) / 2
        else:
            return self.find_index(nums1, nums2, 0, 0, len_nums // 2)
