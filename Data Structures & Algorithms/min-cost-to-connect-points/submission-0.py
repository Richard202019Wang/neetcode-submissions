class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = {i : [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        result = 0
        minheap = [[0, 0]]
        visit = set()
        while len(visit) < N:
            cost, point = heapq.heappop(minheap)
            if point in visit:
                continue
            visit.add(point)
            result += cost
            for neighcost, neigh in adj_list[point]:
                heapq.heappush(minheap, [neighcost, neigh])
        return result
        