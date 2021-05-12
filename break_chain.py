
class Solution():
    # write your code in Python 3.6

    def break_chain(self, A: int) -> int:
        length = len(A)
        dp = [0]*(length-2)

        for i in range(length-2):
            dp[i]=A[i]+A[i+2]

        for i in range(length-2):
            for j in range(i+3, length):
                   
                curr = A[i] + A[j]

                dp[i] = min(curr, dp[i])
                
        return min(dp)

A = [5, 2, 4, 6, 3, 7]

ob = Solution()
ans = ob.break_chain(A)

ans