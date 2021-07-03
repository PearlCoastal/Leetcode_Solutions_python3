#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:

        if not coins:
            return 0
        size = len(coins)
        dp = [[float('inf') for i in range(amount + 1)] for j in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = 0

        for i in range(1, size + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]
            
# @lc code=end

coins = [1, 2, 5]
amount = 11

# coins = [2]
# amount = 3

ob = Solution()
ans = ob.coinChange(coins, amount)
ans