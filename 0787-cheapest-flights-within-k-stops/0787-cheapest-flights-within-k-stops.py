class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (cost, city, stops_used)
        pq = [(0, src, 0)]
        # Record the minimum cost to reach a city with a certain number of stops
        best = {} 
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            if city == dst:
                return cost
            
            if stops > k:
                continue
                
            # Pruning: if we've reached this city before with fewer or equal stops and lower cost, skip
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue
            best[(city, stops)] = cost
            
            for neighbor, price in graph[city]:
                heapq.heappush(pq, (cost + price, neighbor, stops + 1))
        
        return -1