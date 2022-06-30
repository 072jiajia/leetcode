cache = [1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n < len(cache):
            return cache[n]
        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        cache.append(ans)
        return ans
