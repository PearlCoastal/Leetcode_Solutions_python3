
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

A = [7,1,2,8]
ob = Solution()
ans = ob.solve(A)
ans