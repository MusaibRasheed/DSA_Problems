from typing import List
import heapq
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    ways[v] = ways[u]
                    heapq.heappush(heap, (dist[v], v))
                elif d + w == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD