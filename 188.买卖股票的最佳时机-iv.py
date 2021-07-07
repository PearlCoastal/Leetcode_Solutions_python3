#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, K: int, prices: [int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(2)] for k in range(K + 1)] for i in range(n + 1)]
        
        # init
        for k in range(K + 1):
            dp[0][k][0] = 0
            dp[0][k][1] = -float('inf')
        
        for i in range(1, n + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')

            for k in range(1, K + 1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i - 1])

        return dp[n][K][0]

# @lc code=end
k = 2
prices = [2,4,1]

ob = Solution()
ans = ob.maxProfit(k, prices)
ans
