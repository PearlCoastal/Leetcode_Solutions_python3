#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        two_xor = 0
        for num in nums:
            two_xor ^= num
        
        lastDigit = two_xor & (-two_xor)
        a, b = 0, 0
        for num in nums:
            if num & lastDigit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
        


# @lc code=end
nums = [1,2,1,3,2,5]

ob = Solution()
ans = ob.singleNumber(nums)
ans

'''
异或运算 不需要开辟空间 交换两个元素
        a = 3
        b = 4
        a = a ^ b
        b = a ^ b 
        a = a ^ b
        return [a, b]
'''