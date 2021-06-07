#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        def possible(mid: int) -> bool:
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            
            return time <= h
        
        left, right = 1, max(piles)
        while left <= right:

            mid = (left + right) // 2

            if possible(mid):
                right = mid - 1
            else: 
                left = mid + 1
        return left

# @lc code=end

piles = [3,6,7,11]
H = 8

piles = [30,11,23,4,20]
H = 5

ob = Solution()
ans = ob.minEatingSpeed(piles, H)
ans
