class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            best = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < best:
                    best = min_dist[i]
                    u = i

            visited[u] = True
            total += best

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return total