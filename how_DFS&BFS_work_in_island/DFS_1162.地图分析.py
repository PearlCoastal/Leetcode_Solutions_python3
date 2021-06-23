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
        steps = -1

        queue = collections.deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        if len(queue) == 0 or len(queue) == n ** 2: return steps
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps

# @lc code=end

grid = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]

grid = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
    ]
ob = Solution()
ans = ob.maxDistance(grid)
ans