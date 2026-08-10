from typing import List
 
 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
 
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
 
        return dp[amount]
 
 
if __name__ == "__main__":
    sol = Solution()
 
    print(sol.change(5, [1, 2, 5]))   # Expected: 4
    print(sol.change(3, [2]))          # Expected: 0
    print(sol.change(10, [10]))        # Expected: 1
 
    # Edge cases
    print(sol.change(0, [1, 2, 3]))    # Expected: 1 (one way: use nothing)
    print(sol.change(0, []))           # Expected: 1
    print(sol.change(5, []))           # Expected: 0 (no coins, can't make 5)
 