#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        count = 0
        #visited = [[0] * 0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                #发现新的小岛
                if grid[i][j] == '1':
                    #dfs遍历周围所有的岛，连通区域全部置0
                    self.dfs(grid, i, j)
                    count += 1
            
        return count

    def dfs(self, grid: [[str]], i: int, j: int) -> None:

        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
            return 
        #将grid[i][j] 标记为已经访问过，置0
        grid[i][j] = '0'
        #递归进入其上下左右位置上为 1 的数
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
# @lc code=end

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

ob = Solution()
ans = ob.numIslands(grid)
ans