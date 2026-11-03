class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums) or (target + sum(nums)) % 2 != 0:
            return 0 
        bag_size = (target + sum(nums)) // 2

        dp = [0] * (bag_size + 1)
        dp[0] = 1
        for num in nums:
            for i in range(bag_size, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]