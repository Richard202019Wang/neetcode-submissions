class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        cost = 0
        while minHeap:
            node = heapq.heappop(minHeap)
            if node[1] in visit:
                continue
            visit.add(node[1])
            cost = node[0]

            for v2, w2 in edges[node[1]]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (node[0] + w2, v2))
        return cost if len(visit) == n else -1
