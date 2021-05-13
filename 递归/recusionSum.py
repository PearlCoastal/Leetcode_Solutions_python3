
class Solution():
    def recusionSum(self, n: int) -> int:


        '''
        ans = 0
        while n > 0:
            ans += n
            n -= 1
        return ans
        '''

        if n < 0: return 0

        if n == 1:
            return 1

        return self.recusionSum(n-1) + n
        

n = 10

ob = Solution()
ans = ob.recusionSum(n)

ans

'''
1.  递归的返回值 return

2.  总结规律：sum(N) = sum(N-1) + N

3.  递归出口： if n == 1: return 1

4.  从某种意义上来说，递归可以看作是一个while

'''
