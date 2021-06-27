#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        
        dp = [1] * (len(nums))

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
# @lc code=end

nums = [10,9,2,5,3,7,101,18]
nums = [0]

ob = Solution()
ans = ob.lengthOfLIS(nums)
ans