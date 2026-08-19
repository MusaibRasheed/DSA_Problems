from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(k + 1):
            new_costs = costs[:]
            for u, v, price in flights:
                if costs[u] != float('inf') and costs[u] + price < new_costs[v]:
                    new_costs[v] = costs[u] + price
            costs = new_costs

        return costs[dst] if costs[dst] != float('inf') else -1