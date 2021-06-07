#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x

        while left <= right:

            mid = (left + right) // 2

            #最左查找法
            if mid ** 2 <= x:
                ans = mid
                left = mid + 1
            
            if mid ** 2 > x:
                right = mid - 1
        
        return int(ans)

        
# @lc code=end

x = 8

ob = Solution()
ans = ob.mySqrt(x)
ans
