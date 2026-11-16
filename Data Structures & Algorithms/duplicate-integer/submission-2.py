class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = defaultdict(int)
        for num in nums:
            has[num] += 1
        
        for _, vals in has.items():
            if vals > 1:
                return True
        return False
        