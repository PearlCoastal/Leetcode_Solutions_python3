#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: [int], left: int, right: int) -> int:

        def atMostK(nums: [int], k: int):
            ans = 0
            pre = 0

            for i in range(len(nums)):
                if nums[i] <= k:
                    pre += 1
                else:
                    pre = 0
                ans += pre
            return ans
        
        res = atMostK(nums, right) - atMostK(nums, left - 1)
        return res
# @lc code=end


A = [2, 1, 4, 3]
L = 2
R = 3

ob = Solution()
ans = ob.numSubarrayBoundedMax(A, L, R)
ans