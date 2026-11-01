class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, result = len(nums), nums[0]
        max_dp, min_dp = [0] * n, [0] * n
        max_dp[0], min_dp[0] = nums[0], nums[0]

        for i in range(1, n):
            max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1], min_dp[i - 1] * nums[i])

            result = max(result, max_dp[i])
        
        return result
        
        
        