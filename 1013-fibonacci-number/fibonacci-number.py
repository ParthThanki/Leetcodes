class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * (n + 1)  # Create an array to store Fibonacci numbers
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
