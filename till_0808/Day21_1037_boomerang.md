**思路：**
- 哈希表
- 两点之间距离计算公式

```python
class Solution:
    def numberOfBoomerangs(self, points: [[int]]) -> int:

        if not points: return 

        ans = 0
        length = len(points)
        
        for i in range(length):
            dic = defaultdict(int)
            for j in range(length):
                distance = self.distance(points[i], points[j])

                dic[distance] += + 1
            
            for value in dic.values():
                ans += value * (value - 1)
        return ans

    def distance(self, point1: int, point2: int):

        dx = point1[0] - point2[0]
        dy = point1[1] - point2[1]

        distance = dx **2 + dy **2
        return distance

```

**复杂度分析：**
- 时间复杂度： O(N^2)
- 空间复杂度：O(N)