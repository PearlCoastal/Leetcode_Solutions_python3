#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  
        return dp[-1][-1]
# @lc code=end

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# obstacleGrid = [[0,1],[0,0]]
# # obstacleGrid = [[1]]
# obstacleGrid = [[0,1]]
obstacleGrid = [[0,0],[1,1],[0,0]]

ob = Solution()
ans = ob.uniquePathsWithObstacles(obstacleGrid)
ans