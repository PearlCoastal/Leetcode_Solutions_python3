#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return "".join(ans[::-1])
# @lc code=end

columnNumber = 2147483647

ob = Solution()
ans = ob.convertToTitle(columnNumber)
ans