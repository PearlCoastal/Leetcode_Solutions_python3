#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        n = len(grid)

        def bfs(ii, jj):
            queue = [(ii, jj)]
            seen = set(((ii, jj)))
            dist = 0
            while queue:
                dist += 1
                size = len(queue)
                for _ in range(size):
                    i, j = queue.pop(0)
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                            if grid[x][y] == 1:
                                return dist
                            seen.add((x, y))
                            queue.append((x, y))
            
            return -1
        
        ans = -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cur = bfs(i, j)
                    ans = max(ans, cur)
        
        return ans

# @lc code=end

grid = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
    ]
ob = Solution()
ans = ob.maxDistance(grid)
ans
