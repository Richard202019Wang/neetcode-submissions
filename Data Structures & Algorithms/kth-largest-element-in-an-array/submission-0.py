class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        current = 0
        while k > 0:

            current = heapq.heappop(max_heap)
            k -= 1
        return -current