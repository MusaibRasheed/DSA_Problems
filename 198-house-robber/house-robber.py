class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev1 = 0, 0  # max money up to house i-2, i-1
        
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        
        return prev1