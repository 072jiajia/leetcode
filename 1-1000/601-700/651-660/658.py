class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]

        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) >> 1
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left: left+k]
