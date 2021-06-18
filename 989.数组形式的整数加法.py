#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: [int], k: int) -> [int]:
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            curr_sum = num[i] + k % 10 + carry
            num[i] = curr_sum % 10
            carry = curr_sum // 10
            k //= 10
        
        carry += k
        b = []
        while carry:
            b = [(carry % 10)] + b
            carry //= 10

        return b + num


# @lc code=end

num= [2,1,5]
k = 806

num = [2]
k = 998

ob = Solution()
ans = ob.addToArrayForm(num, k)
ans

'''
1, 2, 3, 4
3, 2, 1, 0

4,5,5

'''