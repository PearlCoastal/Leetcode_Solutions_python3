
**思路：**

- 能力检测二分
- DFS： 查找流通区域
- 最左二分模版

```python
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
```
**复杂度分析：**
- 时间复杂度：O(NlogM)
- 空间复杂度：O(N)

📒笔记：
1.  N是grid的总大小，M是grid中的最大值
2.  解空间：[0， max([max(vex) for vex in grid])], 二维数组求解最大值的方法
3.  DFS在求小岛问题的时候，核心是求解流通区域
