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

            #模版：最左查找
            if mid ** 2 <= x:
                #ans 的位置是left还没+1前，保留left位置的答案
                ans = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return ans
        
# @lc code=end

x = 8

ob = Solution()
ans = ob.mySqrt(x)
ans
