from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != start_color:
                return
            image[x][y] = color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(sr, sc)
        return image