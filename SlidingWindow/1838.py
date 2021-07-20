class Solution:
    def maxFrequency(self, nums: [int], k: int) -> int:
        def check(length):
            for i in range(n+1-length):
                j = i + length - 1
                cur = presum[j + 1] - presum[i]
                t = nums[j] * length
                if t - cur <= k:
                    return True
            return False

        n = len(nums)
        nums.sort()
        presum = [0 for i in range(n + 1)]
        presum[1] = nums[0]
        for i in range(2, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return r

nums = [1,4,8,13]
k = 5

ob = Solution()
ans = ob.maxFrequency(nums, k)
ans