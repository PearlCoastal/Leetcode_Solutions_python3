from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> str:

        if not s: return 0
    
        dic = defaultdict(int)
        max_len = 0
        left, right = 0,0

        for right in range(len(s)):
            
            if s[right] in dic:
                if dic[s[right]] + 1 > left:
                    #滑动窗口起始位置右移至重复字符的下一位
                    left = dic[s[right]] + 1

            #更新字符value为当前位置
            dic[s[right]] = right
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        return s[left: right+1]

                


# s = "abcabcbb"
# s = "pwwkew"
s = "abba"

ob = Solution()
ans = ob.lengthOfLongestSubstring(s)
ans

'''
        max_len = 0
        curr_len = 0

        lookup = set()
        left = 0

        for i in range(len(s)):
            curr_len += 1

            # slide window
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curr_len -= 1
            
            lookup.add(s[i])
            max_len = max(max_len, curr_len)

        return max_len
    '''