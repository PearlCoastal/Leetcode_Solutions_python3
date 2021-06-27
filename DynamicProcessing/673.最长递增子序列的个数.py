#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: [int]) -> int:
        
        dp = [[1, 1] for i in range(len(nums))]
        #longest初始化为1，不是0，因为最短也是自己一个数
        longest = 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    #上升子序列加上新的j之后比原来j的要长
                    if dp[i][0] + 1 > dp[j][0]:
                        dp[j][0] = dp[i][0] + 1
                        dp[j][1] = dp[i][1]
                        #更新longest为最长的子序列长度
                        longest = max(longest, dp[j][0])
                    #上升子序列加上j之后和j一样长
                    elif dp[i][0] + 1 == dp[j][0]:
                        dp[j][1] += dp[i][1]
        ans = 0
        for i in range(len(nums)):
            if dp[i][0] == longest:
                ans += dp[i][1]
        
        return ans
        
# @lc code=end

nums = [1,3,5,4,7]
nums = [2,2,2,2,2]

ob = Solution()
ans = ob.findNumberOfLIS(nums)
ans