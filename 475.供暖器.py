#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
from bisect import bisect_right
# @lc code=start
class Solution:
    def findRadius(self, houses: [int], heaters: [int]) -> int:

        houses.sort()
        Heater_position = len(heaters)
        Houses_num = len(houses)

        def possible(diameters: int) -> bool:
            
            for i in range(Heater_position):
                start = heaters[i]
                end = start + diameters
                idx = bisect_right(houses, end)
                if idx >= Houses_num:
                    return True
    
            return False
        
        left, right = 0, houses[-1] - heaters[0]
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return left / 2


# @lc code=end

houses = [1,2,3]
heaters = [2]

ob = Solution()
ans = ob.findRadius(houses, heaters)
ans