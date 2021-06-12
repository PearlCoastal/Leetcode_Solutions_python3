#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#

# @lc code=start
from collections import defaultdict
class Solution:
    def minSubarray(self, nums: [int], p: int) -> int:

        total = sum(nums)
        if total < p:
            return -1
        
        target = total % p
        if target == 0:
            return 0
        
        pre, ans = 0, len(nums)
        dic = defaultdict(int)
        dic = {0: -1}

        for index, element in enumerate(nums):
            pre += element

            dic[pre % p] = index

            if (pre - total) % p in dic:
                ans = min(ans, index - dic[(pre - total) % p])
            
        return ans if ans != len(nums) else -1

# @lc code=end

