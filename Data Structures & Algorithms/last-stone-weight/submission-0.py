class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        if len(stones) <= 1:
            return stones[0] if stones else 0
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            left = -abs(stone1 - stone2)
            if left != 0:
                heapq.heappush(max_heap, left)
        return -max_heap[0] if max_heap else 0