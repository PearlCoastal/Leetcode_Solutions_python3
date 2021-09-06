class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        left = 0
        window = 0
        for right in range(1, len(s)):
            window += 1
            while left < right and s[left] == s[right]:
                window -= 1
                left += 1
            ans = max(ans, window)
        return ans

s = "abccd"
s = "bbbbb"
s = "abcabcbb"

ob = Solution()
ans = ob.lengthOfLongestSubstring(s)
ans