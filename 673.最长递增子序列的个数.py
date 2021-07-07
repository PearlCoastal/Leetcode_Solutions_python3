#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: [int]) -> int:

        if not nums:
            return 0
        size = len(nums)
        dp = [[1, 1] for i in range(nums)]

        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] < nums[j]:
                    dp[i][0] += 1
                    if dp[i][1] + 1 == dp[j][1]
        

# @lc code=end

nums = [1,3,5,4,7]

ob = Solution()
ans = ob.findNumberOfLIS(nums)
ans