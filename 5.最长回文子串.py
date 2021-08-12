#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        ans = s[0]
        
        def extend(left, right, s):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        for i in range(len(s) - 1):
            odd = extend(i, i, s)
            even = extend(i, i + 1, s)
            if max(len(odd), len(even)) > len(ans):
                ans = odd if len(odd) > len(even) else even
        return ans
 

# @lc code=end
s = "babad"

ob = Solution()
ans = ob.longestPalindrome(s)
ans

