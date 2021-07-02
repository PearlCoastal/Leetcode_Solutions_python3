#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: [int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        dp = [[False for i in range(target + 1)] for j in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len(nums)][target]
        
# @lc code=end

nums = [1,5,11,5]

ob = Solution()
ans = ob.canPartition(nums)
ans