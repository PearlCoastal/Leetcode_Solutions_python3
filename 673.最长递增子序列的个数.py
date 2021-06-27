#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: [int]) -> int:

        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1 :
                    count[i] += count[j]
               
        
        longest = max(dp)
        ans = 0
        for i in range(len(nums)):
            if dp[i] == longest:
                ans += count[i]

        return ans
        
# @lc code=end

nums = [1,3,5,4,7]
nums = [2,2,2,2,2]

ob = Solution()
ans = ob.findNumberOfLIS(nums)
ans