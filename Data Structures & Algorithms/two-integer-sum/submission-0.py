class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_left = {}
        for i in range(len(nums)):
            dict_left[nums[i]] = i
        
        for i, num in enumerate(nums):
            left = target - num
            if left in dict_left and dict_left[left] != i:
                return [i, dict_left[left]]
        return []