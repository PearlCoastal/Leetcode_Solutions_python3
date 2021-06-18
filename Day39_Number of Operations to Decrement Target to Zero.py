
class Solution:
    def solve(self, nums, target):
        
        n = len(nums)

        if not target: return 0 

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        prefix[0] = 0
        suffix[0] = 0
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            suffix[i + 1] = suffix[i] + nums[n - i - 1]

        if prefix[n] < target: return -1

        ans, cur = float('inf'), float('inf')

        for i in range(n):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if prefix[i] + suffix[mid] == target:
                    curr = i + mid
                    break
                elif prefix[i] + suffix[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            ans = min(ans, curr)
        
        return -1 if ans == float('inf') else ans
        

nums = [3, 1, 1, 2, 5, 1, 1]
target = 7

ob = Solution()
ans = ob.solve(nums, target)
ans