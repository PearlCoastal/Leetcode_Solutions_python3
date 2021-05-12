

class Solution:

    def lengthOfLIS(self, nums: [int]) -> int:

        length_of_nums = len(nums)

        dp = [1]*(length_of_nums)
        dp

        for i in range(length_of_nums):
            for elements in range(i):

                if(nums[i] > nums[elements]):
                    dp[i] = max(dp[i], dp[elements] + 1)

        return max(dp)

nums = [10,9,2,5,3,7,101,18]

# nums = [0,1,0,3,2,3]

# nums = [7,7,7,7,7,7,7]

# nums = [4,10,4,3,8,9]

ob = Solution()
ans = ob.lengthOfLIS(nums)
ans