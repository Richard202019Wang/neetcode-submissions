class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        steps = 1
        i = 0
        while i + nums[i] < len(nums) - 1:
            cur_max = -float("inf")
            next_i = i
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    if nums[i + j] + i + j >= cur_max:
                        cur_max = nums[i + j] + i + j
                        next_i = i + j
            i = next_i
            steps += 1
        return steps
        