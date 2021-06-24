#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1: return False
        dic = {'(': ')', '{': '}', '[': ']', '?': '?'}
        #防止字符串第一个数就是右括号，栈为空报错
        stack = ['?']

        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        
        return True if len(stack) == 1 else False
# @lc code=end

s = "()[]{}"
s = "([)]"
s = "{[]}"
s = "["
s = "){"

ob = Solution()
ans = ob.isValid(s)
ans