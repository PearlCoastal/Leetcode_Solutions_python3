class Solution():
    def factorialN(self, n: int) -> int:

        if n < 0: return 0

        if n == 1 or n == 0:
            return 1

        return n* self.factorialN(n-1)

n = 10

ob = Solution()
ans = ob.factorialN(n)

ans

'''
1.  0的阶乘为1

'''