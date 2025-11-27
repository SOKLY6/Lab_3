class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        prev1 = 1
        prev2 = 1
        for i in range(3, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return prev2