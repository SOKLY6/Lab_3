class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        for i in range(1, n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return prev2