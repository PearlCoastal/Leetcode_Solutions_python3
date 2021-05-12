class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:

        if 1 not in nums:
            return 1
        
        nums.sort()
        nums

        length = len(nums)

        for i in range(length-1):

            if(nums[i + 1] - nums[i] > 1 and nums[i] >= 1):
                nums[i]
                return nums[i] + 1
            
        return nums[-1] + 1


nums = [1, 2, 3, 5, 6, 7]

# nums = [-1, -3]

# nums = [3, 4, -1, 1]

ob = Solution()

ans = ob.firstMissingPositive(nums)

ans