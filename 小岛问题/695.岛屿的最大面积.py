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
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        
        return ans

    def dfs(self, grid: [[int]], i: int, j: int) -> int:

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0

        if grid[i][j] == 0: return 0

        grid[i][j] = 0
        up = self.dfs(grid, i + 1, j)
        bottom = self.dfs(grid, i - 1, j)
        right = self.dfs(grid, i, j + 1)
        left = self.dfs(grid, i, j - 1)

        #递归返回小岛上下左右连通区域的小岛面积
        return 1 + sum([up, bottom, left, right])
# @lc code=end

grid =[
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

ob = Solution()
ans = ob.maxAreaOfIsland(grid)
ans