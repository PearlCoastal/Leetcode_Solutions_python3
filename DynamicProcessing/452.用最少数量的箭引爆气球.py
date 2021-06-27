#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        if not points:
            return 0
        points.sort()
        dp = [1] * len(points)
        for i in range(len(points)):
            for j in range(i - 1, -1, -1):
                if points[i][0] > points[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]
ob = Solution()
ans = ob.findMinArrowShots(points)
ans