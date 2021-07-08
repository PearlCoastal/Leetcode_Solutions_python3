class Solution():
    def countSubarray(self, nums: [int]) -> int:

        ans = 1
        pre = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                pre += 1
            else:
                pre = 1
            ans += pre

        return ans

nums = [1,3,2,4]

ob = Solution()
ans = ob.countSubarray(nums)
ans