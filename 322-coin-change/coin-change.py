from typing import List
 
 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [0] + [INF] * amount
 
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
 
        return dp[amount] if dp[amount] != INF else -1
 
 
if __name__ == "__main__":
    sol = Solution()
 
    print(sol.coinChange([1, 2, 5], 11))   # Expected: 3
    print(sol.coinChange([2], 3))           # Expected: -1
    print(sol.coinChange([1], 0))           # Expected: 0
 
    # Extra edge cases
    print(sol.coinChange([1], 1))           # Expected: 1
    print(sol.coinChange([186, 419, 83, 408], 6249))  # Expected: 20 (known tricky case)
    print(sol.coinChange([2, 5, 10, 1], 27))  # Expected: 4  (10+10+5+2)
 