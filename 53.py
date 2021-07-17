class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans += 1
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans

nums = [5,7,7,8,8,10]
target = 8

ob = Solution()
ans = ob.search(nums, target)
ans