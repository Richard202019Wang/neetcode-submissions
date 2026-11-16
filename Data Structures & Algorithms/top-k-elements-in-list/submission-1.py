class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = defaultdict(int)
        result = []
        for num in nums:
            freq_map[num] += 1
        
        for key, vals in freq_map.items():
            heapq.heappush(heap, (-vals, key))
        
        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        
        return result
            
        