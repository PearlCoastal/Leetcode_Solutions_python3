

class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left_odd, right_odd = self.expandAroundCenter(s, i, i)
            left_even, right_even = self.expandAroundCenter(s, i, i + 1)
            if right_odd - left_odd > end - start:
                start, end = left_odd, right_odd
            if right_even - left_even > end - start:
                start, end = left_even, right_even
        return s[start: end + 1]
        #字符串截取：后面的值以前的字符 所以要 end+1


# s = "ababa"
# s = "cbbd"
s = "abba"
# s = "a"
# s = "ac"

ob = Solution()
ans = ob.longestPalindrome(s)

ans