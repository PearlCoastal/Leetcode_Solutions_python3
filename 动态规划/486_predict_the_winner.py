class Solution:
    def PredictTheWinner(self, nums: [int]) -> bool:

        length = len(nums)

        dp = [[0]*length for i in range(length)]

        for i in range(length):
            dp[i][i] = nums[i]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length, 1):

                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        
        return dp[0][length-1] >= 0



nums = [1, 5, 2]
# nums = [1, 5, 233, 7]
nums = [0]

ob = Solution()
ans = ob.PredictTheWinner(nums)

ans

'''
1. 预测赢家和石子游戏的区别：石子游戏不可能平局， 所以最后答案一定不等于0

'''