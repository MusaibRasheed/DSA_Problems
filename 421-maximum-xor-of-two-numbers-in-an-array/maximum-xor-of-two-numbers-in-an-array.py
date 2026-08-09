class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Build the answer bit by bit, from the most significant bit down
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            candidate = max_xor | (1 << i)
            
            # Check if any two prefixes XOR to give this candidate
            if any((candidate ^ p) in prefixes for p in prefixes):
                max_xor = candidate
        
        return max_xor