#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        
        if not grid: return 0
        ans = 0
        def dfs(grid:[[int]], i: int, j: int) -> int:

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            up = dfs(grid, i - 1, j)
            down = dfs(grid, i + 1, j)
            left = dfs(grid, i, j - 1)
            right = dfs(grid, i, j + 1)

            return 1 + up + down + left + right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, dfs(grid, i, j))
        return ans

# @lc code=end

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

grid = [[0,0,0,0,0,0,0,0]]
ob = Solution()
ans = ob.maxAreaOfIsland(grid)
ans