#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: [[int]]) -> int:
        
        left, right = 0, max([max(vec) for vec in grid])

        seen = set()

        def test(mid, x, y):
            if x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0:
                return False
            if grid[x][y] > mid:
                return False
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return True
            if (x, y) in seen:
                return False
            seen.add((x, y))
            ans = test(mid, x + 1, y) or test(mid, x - 1, y) or test(mid, x, y + 1) or test(mid, x, y - 1)
            return ans

        while left <= right:
            mid = (left + right) // 2
            if test(mid, 0, 0):
                right = mid - 1
            else:
                left = mid + 1
            seen = set()
        return left
# @lc code=end

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
grid = [[0,2],[1,3]]

ob = Solution()
ans = ob.swimInWater(grid)
ans
