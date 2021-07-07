#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # k = 1

        n = len(prices)
        dp = [[0 for _ in range(2)] for i in range(n + 1)]
        
        dp[0][1] = -float('inf')

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i - 1])
            dp[i][1] = max(dp[i-1][1], -prices[i - 1])
        
        return dp[-1][0]

# @lc code=end

prices = [7,1,5,3,6,4]


ob = Solution()
ans = ob.maxProfit(prices)
ans