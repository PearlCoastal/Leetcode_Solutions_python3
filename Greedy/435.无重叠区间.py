#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        
        size = len(intervals)
        if size == 0 or size == 1: return 0

        intervals.sort(key = lambda x: x[1])
        # [1,2],[1,3],[2,3],[3,4]
        ans = 0
        end = intervals[0][1]
        for i in range(1, size):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                ans += 1

        return ans

# @lc code=end

intervals = [ [1,2], [2,3], [3,4], [1,3] ]
# intervals = [ [1,2], [1,2], [1,2] ]
# intervals = [ [1,2], [2,3] ]

ob = Solution()
ans = ob.eraseOverlapIntervals(intervals)
ans