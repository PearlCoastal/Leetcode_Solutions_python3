
class Solution:
    def solve(self, nums, target):
        if not nums:
            return 0 if target == 0 else -1

        if sum(nums) < target:
            return -1
        
        left = 0
        left_sum = 0
        while left < len(nums) and left_sum < target:
            left_sum += nums[left]
            left += 1
        
        ans = left if left_sum == target else float('inf')

        right = len(nums)
        right_sum = 0

        while left > 0:
            left -= 1
            left_sum -= nums[left]

            while right >= left and left_sum + right_sum < target:
                right -= 1
                right_sum += nums[right]
            
            if left_sum + right_sum == target:
                ans = min(ans, left + len(nums) - right)
            
        return ans if ans != float('inf') else -1

        

nums = [3, 1, 1, 2, 5, 1, 1]
target = 7

ob = Solution()
ans = ob.solve(nums, target)
ans