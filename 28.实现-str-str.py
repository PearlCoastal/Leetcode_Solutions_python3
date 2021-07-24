#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        # next table
        table = [0 for i in range(len(needle))]
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = table[j - 1]
            
            if needle[i] == needle[j]:
                j += 1
            
            table[i] = j
        
        # match
        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = table[j - 1]
            
            if haystack[i] == needle[j]:
                j += 1
            
            if j == len(needle):
                return i - len(needle) + 1
        
        return -1

# @lc code=end

haystack = "aaabbab"
needle = "aaabbab"

ob = Solution()
ans = ob.strStr(haystack, needle)
ans