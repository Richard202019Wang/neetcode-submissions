class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_len = 1
                while cur_len + num in num_set:
                    cur_len += 1
                result = max(result, cur_len)
        return result
        