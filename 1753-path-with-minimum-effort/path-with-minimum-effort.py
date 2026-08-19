from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        heap = [(0, 0, 0)]  # (effort, row, col)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            curr_effort, x, y = heapq.heappop(heap)

            if x == rows - 1 and y == cols - 1:
                return curr_effort

            if curr_effort > effort[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(curr_effort, abs(heights[nx][ny] - heights[x][y]))
                    if new_effort < effort[nx][ny]:
                        effort[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))

        return 0