#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
import collections
# @lc code=start
class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        
        n = len(grid)
        q = collections.deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        if len(q) == 0 or len(q) == n ** 2: return -1
        step = -1
        while q:
            step += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for cur_i, cur_j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if cur_i >= 0 and cur_i < n and cur_j >= 0 and cur_j < n and grid[cur_i][cur_j] == 0:
                        q.append((cur_i, cur_j))
                        grid[cur_i][cur_j] = -1
        
        return step



# @lc code=end

grid = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
    ]
ob = Solution()
ans = ob.maxDistance(grid)
ans
