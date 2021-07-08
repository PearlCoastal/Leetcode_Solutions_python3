class Solution():
    def countSubarray(self, nums: [int]) -> int:

        ans = 0
        pre = 0

        for element in nums:
            pre += 1
            ans += pre

        return ans

nums = [1,3,4]

ob = Solution()
ans = ob.countSubarray(nums)
ans