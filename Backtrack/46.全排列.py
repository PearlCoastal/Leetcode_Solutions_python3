#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: [int]) -> [[int]]:

        length = len(nums)
        
        nums.sort()
        path = []
        ans = []

# @lc code=end

nums = [1,2,3]
ob = Solution()
ans = ob.permute(nums)
ans