#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: [[int]]) -> [[int]]:
        m, n = len(matrix), len(matrix[0])

        dp = [[float('inf') for i in range(n)] for j in range(m)]

        # init
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
        
        # start --> end
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        #end --> start
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 <= m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 <= n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        
        return dp

# @lc code=end

mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
    ]

ob = Solution()
ans = ob.updateMatrix(mat)
ans