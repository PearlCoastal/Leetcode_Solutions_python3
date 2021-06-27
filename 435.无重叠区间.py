#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:

        intervals.sort()
        dp = [1] * len(intervals)

        for i in range(len(intervals)):
            # 注意已经按照区间开始排好序了，所以在做比较的时候就可以剪枝
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
        
        ans = len(intervals) - max(dp)
        return ans
               

# @lc code=end

intervals = [ [1,2], [2,3], [3,4], [1,3] ]
intervals = [ [1,2], [1,2], [1,2] ]
intervals = [ [1,2], [2,3] ]
intervals = [ [0,1],[3,4],[1,2] ] 

ob = Solution()
ans = ob.eraseOverlapIntervals(intervals)
ans