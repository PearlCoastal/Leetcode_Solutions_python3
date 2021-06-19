#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start

import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:

        target = collections.Counter(p)
        ans = []

        for i in range(len(s)):
            if i >= len(p):
                target[s[i - len(p)]] += 1

                if target[s[i - len(p)]] == 0:
                    del target[s[i - len(p)]]

            target[s[i]] -= 1
            if target[s[i]] == 0:
                del target[s[i]]
            
            if len(target) == 0:
                ans.append(i - len(p) + 1)
        return ans

        

# @lc code=end

s = "baa" 
p =  "aa"

# s = "cbaebabacd"
# p = "abc"

ob = Solution()
ans = ob.findAnagrams(s, p)
ans

