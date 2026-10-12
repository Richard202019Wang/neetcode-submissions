class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_list = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq_map.items():
            freq_list[cnt].append(num)
        
        result = []
        for i in range(len(freq_list ) - 1, 0, -1):
            for num in freq_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
        