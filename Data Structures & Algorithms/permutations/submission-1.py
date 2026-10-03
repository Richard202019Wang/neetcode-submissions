class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        choose_list = [False] * len(nums)
        def dfs(i):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return 
            if i >= len(nums):
                return 
            
            for idx in range(len(nums)):
                if not choose_list[idx]:
                    subset.append(nums[idx])
                    choose_list[idx] = True
                    dfs(i + 1)
                    subset.pop()
                    choose_list[idx] = False
                else:
                    continue
        dfs(0)
        return result