class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n  # longest prefix-suffix array
        
        # Build the LPS array (same as in KMP)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # The last value in lps gives the length of longest happy prefix
        return s[:lps[-1]]
