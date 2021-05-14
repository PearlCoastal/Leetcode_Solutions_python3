
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        if(not s): max_len = 0

        length = len(s)
        curr_len = 0

        lookup = set()
        left = 0

        for i in range(length):
            curr_len += 1

            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curr_len -=1

            lookup.add(s[i])
            max_len = max(max_len, curr_len)

        return max_len
        

s = "abcabcbb"
s = "abcdefghhhhhh"
# s = "bbbbb"
# s = "pwwkew"

ob = Solution()
ans = ob.lengthOfLongestSubstring(s)

ans

'''
ATTENTION

0. sliding window

1. set()

2. add() in set

3. remove() in set

4. how while() works inside the function

'''