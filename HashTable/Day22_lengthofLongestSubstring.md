**思路：**
- 滑动窗口：left, right
- 字典 dic = {字符：位置}
- 最大长度max_len = right - left + 1

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

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

```

**复杂度分析：**

- 时间复杂度：O(N)
- 空间复杂度：O(N)