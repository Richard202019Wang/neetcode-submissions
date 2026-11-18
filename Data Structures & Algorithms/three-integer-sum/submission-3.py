class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                Tsum = nums[l] + num + nums[r]

                if Tsum > 0:
                    r -= 1
                elif Tsum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result