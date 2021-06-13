#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ["a", "e", "i", "o", "u"]

        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1

        ans = cur
        for i in range(k, len(s)):
            cur += 1 if s[i] in vowels else 0
            cur -= 1 if s[i-k] in vowels else 0
            ans = max(ans, cur)
        
        return ans

# @lc code=end

s = "abciiidef"
k = 3

ob = Solution()
ans = ob.maxVowels(s, k)
ans

