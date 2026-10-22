class Solution:
    def networkDelayTime(self, times, n, k):
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # Relax edges N-1 times
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
        # Find the maximum time among all nodes
        max_time = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1 # Some node is unreachable
            max_time = max(max_time, dist[i])
            
        return max_time