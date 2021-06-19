#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
import collections
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = collections.defaultdict(int)
        for char in t:
            required[char] += 1
        
        have = collections.defaultdict(int)
        left, right = 0, 0
        count = 0
        ans = (float('inf'), None, None)

        while right < len(s):
            cur = s[right]
            if cur in required:
                have[cur] += 1
                if have[cur] == required[cur]:
                    count += 1
            
            while count == len(required):
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                prev = s[left]
                if prev in required:
                    have[prev] -= 1
                    if have[prev] < required[prev]:
                        count -= 1
            
                left += 1
            
            right += 1
        
        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]:ans[2] + 1]

# @lc code=end

s = "ADOBECODEBANC"
t = "ABC"

ob = Solution()
ans = ob.minWindow(s, t)
ans