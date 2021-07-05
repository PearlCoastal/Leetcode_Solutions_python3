#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        
        # [i][j]
        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]
        # @lc code=end

grid = [[1,3,1],[1,5,1],[4,2,1]]

ob = Solution()
ans = ob.minPathSum(grid)
ans