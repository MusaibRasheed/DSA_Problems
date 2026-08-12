from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr_max = 0
            for length in range(1, min(k, i) + 1):
                curr_max = max(curr_max, arr[i - length])
                dp[i] = max(dp[i], dp[i - length] + curr_max * length)

        return dp[n]