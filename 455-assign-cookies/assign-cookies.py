from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # pointer into children (greed factors)
        j = 0  # pointer into cookies (sizes)
        content = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content