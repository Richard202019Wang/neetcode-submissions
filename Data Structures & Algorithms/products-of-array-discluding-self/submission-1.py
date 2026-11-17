class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_p = [1] * len(nums)
        suffix_p = [1] * len(nums)
        prefix_p[0] = nums[0]
        suffix_p[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix_p[i] = prefix_p[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix_p[i] = suffix_p[i + 1] * nums[i]
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_p[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix_p[i - 1])
            else:
                result.append(prefix_p[i - 1] * suffix_p[i + 1])
        return result
        