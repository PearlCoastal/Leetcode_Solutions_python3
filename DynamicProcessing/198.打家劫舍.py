#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: [int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        pre = max(nums[0], nums[1])
        prepre = pre
        for i in range(len(nums)):
            ans = max(prepre + nums[i], pre)
            pre = ans
        
        return ans
# @lc code=end

nums = [2,7,9,3,1]
nums = [1,2,3,1]
nums = [0]
nums = [2,1,1,2]

ob = Solution()
ans = ob.rob(nums)
ans
