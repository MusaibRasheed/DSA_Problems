from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        boundaries = sorted(cuts + [0, n])
        m = len(boundaries)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if j - i <= 1:
                return 0
            best = float('inf')
            for k in range(i + 1, j):
                cost = dp(i, k) + dp(k, j) + (boundaries[j] - boundaries[i])
                best = min(best, cost)
            return best

        return dp(0, m - 1)