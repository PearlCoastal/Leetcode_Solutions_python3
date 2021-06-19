#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:

        if k == len(cardPoints): return sum(cardPoints)

        stay, curSum = 0, 0
        window_size = len(cardPoints) - k
        for right in range(window_size):
            curSum += cardPoints[right]
        stay = curSum

        for right in range(window_size, len(cardPoints)):
            curSum += cardPoints[right]
            curSum -= cardPoints[right - window_size]
            stay = min(stay, curSum)
        
        return (sum(cardPoints) - stay)

# @lc code=end

# cardPoints = [1,2,3,4,5,6,1]
# k = 3

cardPoints = [1,79,80,1,1,1,200,1]
k = 3

ob = Solution()
ans = ob.maxScore(cardPoints, k)
ans

'''
要求手里的点数最大 == 剩下的卡牌数之和 最小
'''