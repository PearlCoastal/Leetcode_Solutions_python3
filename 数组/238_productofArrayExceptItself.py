class Solution:

    def productExceptSelf(self, nums: [int]) -> [int]:
        
        length = len(nums)

        result = [1]* length
        R = 1
        
        for i in range(1, length):
            result[i] = nums[i-1] * result[i-1]

        for j in reversed(range(length)):
            
            result[j] = result[j] * R
            R *= nums[j]

        return result


nums = [1, 2, 3, 4]

ob = Solution()
ans = ob.productExceptSelf(nums)

ans

'''
1. 正序向后求得时候只需要 当前值的前一位数叠乘

2. 逆序向前求的时候需要R 来保存当前值后面所有数的乘积

'''