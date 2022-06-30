from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m):
            nums1[m+n-1-i], nums1[m-1-i] = nums1[m-1-i], nums1[m+n-1-i]

        i1 = 0
        i2 = 0
        while i1 < m and i2 < n:
            if nums1[i1 + n] < nums2[i2]:
                nums1[i1 + i2] = nums1[i1 + n]
                i1 += 1
            else:
                nums1[i1 + i2] = nums2[i2]
                i2 += 1
        while i2 < n:
            nums1[i1 + i2] = nums2[i2]
            i2 += 1
