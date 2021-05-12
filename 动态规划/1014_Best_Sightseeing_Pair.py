

class Solution:
    def maxScoreSightseeingPair(self, values: [int]) -> int:

        length = len(values)

        '''
        dp = [0]*length
        for i in range(length):
            for j in range(i+1,length):

                curr_sum = values[i] + values[j] + i - j
                if(curr_sum > dp[i]): dp[i] = curr_sum

        return max(dp)

        超出时间限制
        '''
        max_score = curr_max = values[0] + 0

        for j in range(1, length):

            if(curr_max + values[j] - j > max_score): max_score = curr_max + values[j] - j

            if(curr_max < values[j] + j): curr_max = values[j] + j
            '''
            这里没有判断当前的景点+距离值 就更新 所以错误
            curr_max = values[j] + j
            '''

        return max_score


# values = [8,1,5,2,6]
# values = [1,2]
values = [2,7,7,2,1,7,10,4,3,3]

ob = Solution()
ans = ob.maxScoreSightseeingPair(values)

ans