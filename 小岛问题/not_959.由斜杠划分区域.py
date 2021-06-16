#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#

# @lc code=start
class Solution:
    def regionsBySlashes(self, grid: [str]) -> int:
        m, n = len(grid), len(grid[0])
        new_grid = [[0 for _ in range(3 * n)] for _ in range(3 * m)]
        ans = 0
        # 预处理，生成新的 3 * m * 3 * n 的网格
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    new_grid[3 * i][3 * j + 2] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j] = 1
                if grid[i][j] == '\\':
                    new_grid[3 * i][3 * j] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j + 2] = 1
        def dfs(i, j):
            if 0 <= i < 3 * m and 0 <= j < 3 * n and new_grid[i][j] == 0:
                new_grid[i][j] = 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        for i in range(3 * m):
            for j in range(3 * n):
                if new_grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans
# @lc code=end

grid = [
  "/\\",
  "\\/"
]

ob = Solution()
ans = ob.regionsBySlashes(grid)
ans