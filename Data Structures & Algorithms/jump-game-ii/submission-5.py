class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        steps = 1
        i = 0
        while i + nums[i] < len(nums) - 1:
            cur_max_reach = -float("inf")
            next_i = i
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    reach = (i + j) + nums[i + j] 
                    
                    if reach >= cur_max_reach:
                        cur_max_reach = reach
                        next_i = i + j
            i = next_i
            steps += 1
        return steps
        