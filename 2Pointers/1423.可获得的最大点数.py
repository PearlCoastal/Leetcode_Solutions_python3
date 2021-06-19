#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:

        if not cardPoints or not k: return

        left, right = 0, len(cardPoints) - 1
        leftSum, rightSum = 0, 0
        ans = 0

        for left in range(k):
            leftSum += cardPoints[left]
        ans = max(ans, leftSum)

        while left > -1:
            leftSum -= cardPoints[left]
            left -= 1

            while right >= left and (left + len(cardPoints) - right) + 1 == k:
                
                rightSum += cardPoints[right]
                right -= 1

            ans = max(ans, leftSum + rightSum)
            
        return ans
        

# @lc code=end

cardPoints = [1,2,3,4,5,6,1]
k = 3

cardPoints = [9,7,7,9,7,7,9]
k = 7

ob = Solution()
ans = ob.maxScore(cardPoints, k)
ans