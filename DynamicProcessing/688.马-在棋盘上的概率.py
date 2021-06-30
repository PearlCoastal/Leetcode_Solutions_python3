#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] “马”在棋盘上的概率
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dp = [[0 for i in range(n)] for j in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            temp = [[0 for i in range(n)] for j in range(n)]

            for i in range(n):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    
                    for x, y in [(i + 2, j + 1), (i + 2, j - 1), (i - 2, j + 1), (i - 2, j - 1), (i + 1, j + 2), (i - 1, j + 2), (i + 1, j - 2), (i - 1, j - 2)]:
                        if 0 <= x < n and 0 <= y < n:
                            temp[x][y] += dp[i][j] / 8
                
            dp = temp
        
        ans = 0 
        for line in dp:
            ans += sum(line)
        return ans

# @lc code=end

n = 3
k = 2
row = 0
column = 0

ob = Solution()
ans = ob.knightProbability(n, k, row, column)
ans