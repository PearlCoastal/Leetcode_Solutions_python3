'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length_of_s = len(s)
        dp = [[False] * length_of_s for _ in range(length_of_s)]
        ans = ""

        for length_of_substring in range(length_of_s):
            for begin_of_result in range(length_of_s):
                end_of_result = begin_of_result + length_of_substring
                if end_of_result >= len(s):
                    break
                if length_of_substring == 0:
                    dp[begin_of_result][end_of_result] = True
                elif length_of_substring == 1:
                    dp[begin_of_result][end_of_result] = (s[begin_of_result] == s[end_of_result])
                else:
                    dp[begin_of_result][end_of_result] = (dp[begin_of_result + 1][end_of_result - 1] and s[begin_of_result] == s[end_of_result])
                if dp[begin_of_result][end_of_result] and length_of_substring + 1 > len(ans):
                    ans = s[begin_of_result:end_of_result+1]
        return ans
'''

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