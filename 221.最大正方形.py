#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:

        length, width = len(matrix), len(matrix[0])
        dp = [[0 for i in range(width)] for j in range(length)]

        for i in range(length):
            if matrix[i][0] == '1':
                dp[i][0] = 1

        for j in range(width):
            if matrix[0][j] == '1':
                dp[0][j] = 1

        #(i-1,j-1),(i-1,j)
        #(i, j-1), (i,j)
        for i in range(1, length):
            for j in range(1, width):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        ans = 0
        for i in range(length):
            for j in range(width):
                ans = max(ans, dp[i][j])
        return ans ** 2
# @lc code=end

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]

ob = Solution()
ans = ob.maximalSquare(matrix)
ans