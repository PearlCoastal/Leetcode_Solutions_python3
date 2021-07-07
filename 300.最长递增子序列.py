#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:

        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size

        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

# @lc code=end

nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]

ob = Solution()
ans = ob.lengthOfLIS(nums)
ans