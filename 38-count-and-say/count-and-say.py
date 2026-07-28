class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Get the previous sequence
        prev = self.countAndSay(n - 1)
        result = []
        
        # Run-length encoding
        i = 0
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            result.append(str(count) + prev[i])
            i += 1
        
        return "".join(result)
