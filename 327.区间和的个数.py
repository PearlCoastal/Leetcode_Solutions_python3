#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from sortedcontainers import SortedList
# @lc code=start
class Solution:
    def countRangeSum(self, nums: [int], lower: int, upper: int) -> int:

        ans, pre, cur = 0, SortedList(), 0
        for a in nums:
            cur += a
            lo = pre.bisect_right(cur - lower)
            up = pre.bisect_left(cur - upper)
            ans += (lo - up)
            pre.add(cur)
        return ans
# @lc code=end

nums = [-2,5,-1]

lower = -2

upper = 2

ob = Solution()
ans = ob.countRangeSum(nums, lower, upper)
ans
