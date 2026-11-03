class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        bag_sum = sum(nums) 
        if bag_sum % 2 != 0:
            return False
        half = bag_sum // 2
        
        dp = [0] * (half + 1)
        for num in nums:
            for i in range(half, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + num)
        
        
        return max(dp) == half