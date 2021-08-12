#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#
import collections
# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: [int]) -> int:
        '''
        dp = {index: {diff: count}}
        '''
        dp = [collections.defaultdict(int) for _ in nums]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if dp[j][diff]:
                    ans += dp[j][diff]
        return ans
            
# @lc code=end

nums = [2, 4, 6, 8, 10]

ob = Solution()
ans = ob.numberOfArithmeticSlices(nums)
ans