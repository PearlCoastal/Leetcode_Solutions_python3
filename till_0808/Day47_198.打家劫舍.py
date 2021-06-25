#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: [int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 2)
        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        
        return dp[-1]
# @lc code=end

nums = [2,7,9,3,1]
nums = [1,2,3,1]
nums = [0]
nums = [2,1,1,2]

ob = Solution()
ans = ob.rob(nums)
ans
