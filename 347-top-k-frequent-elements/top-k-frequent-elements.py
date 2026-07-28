from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies
        freq = Counter(nums)
        
        # Use a heap to get k most common
        return [num for num, count in freq.most_common(k)]
