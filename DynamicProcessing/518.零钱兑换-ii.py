#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        if not coins:
            return 0
        size = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(size + 1)]
        for i in range(size + 1):
            dp[i][0] = 1
        
        for i in range(1, size + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
# @lc code=end

coins= [1,2,5]
amount = 5

amount = 10
coins = [10] 

amount = 3
coins = [2]

ob = Solution()
ans = ob.change(amount, coins)
ans