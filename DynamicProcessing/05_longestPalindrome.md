LC.5 最长回文子串
====
https://leetcode-cn.com/problems/longest-palindromic-substring/

## 题目描述

## 思路

连续回文子穿麻烦的地方在于处理奇偶。

比如 "aba" "abba" 两种。

- 奇数串的情况： 回文中心是单个字符， 两端字符如果一样就往外延伸。
- 偶数串的情况： 回文中心是两个字符， 首先这两个字符要相同， 然后再向外延伸查看两端字符是否一样。

两端字符 left, right 👇

如果有 s[left] == s[right], 并且 s[left + 1: right] 是回文串， 那么 子串长度 + 2 就是新的回文子串的长度。




## 代码
```python
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
```

## 复杂度分析
- 时间复杂度： O(n^2)
- 空间复杂度： O(n^2)
