class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # prefix counts of single digits and pairs
        prefix_single = [0] * 10
        prefix_pair = [[0] * 10 for _ in range(10)]
        prefix_dp = [ [ [0]*10 for _ in range(10) ] for _ in range(n) ]

        for i, ch in enumerate(s):
            d = int(ch)
            if i > 0:
                for a in range(10):
                    for b in range(10):
                        prefix_dp[i][a][b] = prefix_dp[i-1][a][b]
            for a in range(10):
                prefix_pair[a][d] += prefix_single[a]
                prefix_dp[i][a][d] = prefix_pair[a][d]
            prefix_single[d] += 1

        # suffix counts of single digits and pairs
        suffix_single = [0] * 10
        suffix_pair = [[0] * 10 for _ in range(10)]
        suffix_dp = [ [ [0]*10 for _ in range(10) ] for _ in range(n) ]

        for i in range(n-1, -1, -1):
            d = int(s[i])
            if i < n-1:
                for a in range(10):
                    for b in range(10):
                        suffix_dp[i][a][b] = suffix_dp[i+1][a][b]
            for b in range(10):
                suffix_pair[d][b] += suffix_single[b]
                suffix_dp[i][d][b] = suffix_pair[d][b]
            suffix_single[d] += 1

        # count palindromes
        ans = 0
        for mid in range(2, n-2):
            for a in range(10):
                for b in range(10):
                    left = prefix_dp[mid-1][a][b]
                    right = suffix_dp[mid+1][b][a]
                    ans = (ans + left * right) % MOD

        return ans
