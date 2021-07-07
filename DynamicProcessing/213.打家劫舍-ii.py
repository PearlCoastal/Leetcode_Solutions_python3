#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        def helper(nums: List[int]) -> int:

            dp = [0 for i in range(len(nums) + 2)]

            for i in range(2, len(nums) + 2):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])

            return max(dp)
    
        ans = max(helper(nums[: -1]), helper(nums[1:]))
        return ans
# @lc code=end

