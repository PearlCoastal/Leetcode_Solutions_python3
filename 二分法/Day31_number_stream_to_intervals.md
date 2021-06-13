**思路：**（抄的西法的）

- bisect + sortedlist

```python
import bisect
from sortedcontainers import SortedList

class Solution:
    def solve(self, A):
        d = SortedList()
        ans = 0

        for a in A:
            i = bisect.bisect_right(d, a * 3)
            ans += len(d) - i
            d.add(a)

        return ans
```
**复杂度分析：**
- 时间复杂度：O(logN)
- 空间复杂度：O(N)