

class Solution:
    def maxSubArray(self, nums:[int]) -> int:

        length = len(nums)
        dp = [0]*(length)
    
        for i in range(length):
    
               curr = dp[i-1] + nums[i]

               dp[i] = max(nums[i], curr)
            
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [0]
# nums = [-100000000]

ob = Solution()
ans = ob.maxSubArray(nums)

ans