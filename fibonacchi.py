
class Solution():
    # write your code in Python 3.6

   def findNumbers(self, k: int) -> int:
        a = 0
        b = 0

        fibo = []

        while a + b <= k:

            fibo.append(a + b)
            a, b = a+b, b+1
        return b-1

        # for pos in fibo[::-1]:
        #     if k < fibo[pos]: return pos-1

k=21

ob = Solution()
ans = ob.findNumbers(k)

ans