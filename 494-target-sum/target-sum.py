from typing import List
 
 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
 
        # Impossible cases
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
 
        subset_target = (target + total) // 2
 
        # dp[s] = number of ways to reach sum s
        dp = [0] * (subset_target + 1)
        dp[0] = 1
 
        for num in nums:
            for s in range(subset_target, num - 1, -1):
                dp[s] += dp[s - num]
 
        return dp[subset_target]
 
 
if __name__ == "__main__":
    sol = Solution()
 
    print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))  # Expected: 5
    print(sol.findTargetSumWays([1], 1))                # Expected: 1
 
    # Edge cases
    print(sol.findTargetSumWays([1], 2))                # Expected: 0 (unreachable)
    print(sol.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))  # Expected: 256
    print(sol.findTargetSumWays([100], -100))            # Expected: 1
    print(sol.findTargetSumWays([0], 0))                 # Expected: 2 (+0 and -0 both work)
 