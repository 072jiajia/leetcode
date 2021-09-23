class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = 0
        stack = [0]
        for num in target:
            if num >= stack[-1]:
                count += (num - stack[-1])
                stack[-1] = num
            else:
                while stack[-1] < num:
                    stack.pop(-1)
                stack.append(num)
        return count
