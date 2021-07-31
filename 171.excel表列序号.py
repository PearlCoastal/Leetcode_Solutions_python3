#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = list(columnTitle)
        ans = 0
        for i in range(len(column)):
            ans = ans * 26 + (ord(column[i]) - ord("A") + 1)
        return ans
# @lc code=end

columnTitle = "ABC"

ob = Solution()
ans = ob.titleToNumber(columnTitle)
ans