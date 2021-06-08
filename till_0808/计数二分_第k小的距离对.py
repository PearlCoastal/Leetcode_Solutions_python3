
class Solution:
    def solve(self, nums, k):
        nums.sort()
        
        def cnt_not_greater(mid: int, k: int) -> int:

            leftp = 0
            cnt = 0
            for i in range(1, len(nums)):
                while(nums[i] - nums[leftp] > mid):
                    leftp += 1
                cnt  += i - leftp
            
            return cnt > k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2

            if cnt_not_greater(mid, k):
                right = mid
            else:
                left = mid + 1

        return left


nums = [1,5,3,2]
k = 3



ob = Solution()
ans = ob.solve(nums, k)
ans