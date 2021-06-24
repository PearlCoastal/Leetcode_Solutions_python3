#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:

        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            if i == len(cost):
                dp[i] = min(dp[i - 1], dp[i - 2]) + 0
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return dp[-1]

# @lc code=end

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [10, 15, 20]

ob = Solution()
ans = ob.minCostClimbingStairs(cost)
ans