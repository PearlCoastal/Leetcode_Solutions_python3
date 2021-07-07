#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:

        total = sum(nums)
        if (total + target) % 2 == 1:
            return 0

        target = (total + target) // 2
        dp = [[0 for i in range(target)] for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = 1

        for i in range(len(nums)):
            for j in range(target):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]
# @lc code=end

nums = [1,1,1,1,1]
target = 3

ob = Solution()
ans = ob.findTargetSumWays(nums, target)
ans