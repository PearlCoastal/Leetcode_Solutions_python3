class Solution():
    def atMostK(self, nums: [int], k: int) -> int:

        ans = 0
        pre = 0

        for i in range(1, len(nums)):
            if nums[i] <= k:
                pre += 1
            else:
                pre = 0
            ans += pre
        
        return ans

nums = [1,3,2,4]
k = 4

ob = Solution()
ans = ob.atMostK(nums, k)
ans