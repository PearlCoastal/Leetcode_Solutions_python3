class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        length = len(s)

        left, right = 0, length-1

        while right-left > 0:
            
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]

ob = Solution()
ans = ob.reverseString(s)

ans

'''
1.  简单题
2.  练习原地反转


'''

        

        