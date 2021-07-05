#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:

        g.sort()
        s.sort()
        child, cookie = 0, 0
        ans = 0
        while child < len(g) and cookie < len(s):

            if g[child] <= s[cookie]:
                child += 1
                ans += 1
            cookie += 1
        return ans
# @lc code=end

g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]

# g = [10,9,8,7]
# s = [5,6,7,8]

ob = Solution()
ans = ob.findContentChildren(g, s)
ans