#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution():
    memo = {}
    def climbStairs(self, n: int):
        if n == 1:return 1
        if n == 2: return 2
        
        if n in self.memo: return self.memo[n]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = ans
        return ans



# @lc code=end

n = 10

ob = Solution()
ans = ob.climbStairs(n)
ans