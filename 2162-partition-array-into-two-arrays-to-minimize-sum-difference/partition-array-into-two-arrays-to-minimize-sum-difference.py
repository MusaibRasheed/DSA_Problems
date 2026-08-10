from typing import List
from itertools import combinations
from bisect import bisect_left
 
 
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        n2 = len(nums)
        n = n2 // 2
 
        A = nums[:n]
        B = nums[n:]
 
        def group_by_size(arr: List[int]) -> List[List[int]]:
            """Return groups[i] = sorted list of sums using exactly i elements."""
            m = len(arr)
            groups = [[] for _ in range(m + 1)]
            for size in range(m + 1):
                for combo in combinations(arr, size):
                    groups[size].append(sum(combo))
            for g in groups:
                g.sort()
            return groups
 
        sumsA = group_by_size(A)
        sumsB = group_by_size(B)
 
        best = float('inf')
        half = total / 2.0
 
        for i in range(n + 1):
            need_size = n - i
            right_list = sumsB[need_size]
            if not right_list:
                continue
 
            for left_sum in sumsA[i]:
                # We want left_sum + right_sum as close to `half` as possible
                target = half - left_sum
                pos = bisect_left(right_list, target)
 
                # Check the candidate at pos and pos-1 (closest neighbors)
                for idx in (pos - 1, pos):
                    if 0 <= idx < len(right_list):
                        s = left_sum + right_list[idx]
                        diff = abs(total - 2 * s)
                        if diff < best:
                            best = diff
 
        return best
 
 
if __name__ == "__main__":
    sol = Solution()
 
    print(sol.minimumDifference([3, 9, 7, 3]))          # Expected: 2
    print(sol.minimumDifference([-36, 36]))              # Expected: 72
    print(sol.minimumDifference([2, -1, 0, 4, -2, -9]))  # Expected: 0
 
    # Larger stress test (n = 15, within constraints)
    import random
    random.seed(0)
    big = [random.randint(-10**7, 10**7) for _ in range(30)]
    print("Ran n=15 stress test, result:", sol.minimumDifference(big))
 