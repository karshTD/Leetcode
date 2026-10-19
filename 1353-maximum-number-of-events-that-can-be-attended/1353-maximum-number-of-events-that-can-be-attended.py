
class Solution:
    def maxEvents(self, events):
        events.sort()
        n = len(events)
        i = 0
        day = 0
        count = 0
        heap = []
        max_day = max(e[1] for e in events)
        
        while i < n or heap:
            if not heap:
                day = max(day, events[i][0])
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            heapq.heappop(heap)
            count += 1
            day += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
        
        return count