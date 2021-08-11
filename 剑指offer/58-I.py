class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        while i <= len(s) - 1:
            if s[i] != ' ':
                break
            i += 1
        if i == len(s):
            return ""
        j = len(s) - 1
        while j >= 0:
            if s[j] != ' ':
                break
            j -= 1
        s = s[i: j + 1]
        ans = []
        left = right = len(s) - 1
        while left >= 0:
            if s[left] == ' ' and left != len(s) - 1:
                if s[left + 1] != ' ':
                    ans.append(s[left + 1: right + 1])
                right = left - 1
            
            if left == 0:
                ans.append(s[left: right + 1])
            left -= 1
        return ' '.join(ans)
        
    
s = "   the sky is       blue.   "
# s = " "
ob = Solution()
ans = ob.reverseWords(s)
ans