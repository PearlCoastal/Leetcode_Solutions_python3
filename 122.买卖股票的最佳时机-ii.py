#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:

        ans = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans +=  prices[i] - prices[i - 1]

        return ans
# @lc code=end

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

ob = Solution()
ans = ob.maxProfit(prices)
ans