

class Solution:

    def countBits(self, num: int) -> [int]:

        dp = [0]*(num+1)

        for curr in range(1, num+1):

            if(int(curr%2) == 0): dp[curr] = dp[int(curr/2)]

            else: dp[curr] = dp[curr-1] + 1

        return dp

input = 2

# temp = 2%2
# temp
# temp2 = int(3%2)
# temp2

ob = Solution()
ans = ob.countBits(input)

ans