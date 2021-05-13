class Solution():
    def fibonacci(self, n: int) -> int:

        if n == 1 or n == 2:
            return 1
        
        return self.fibonacci(n-1) + self.fibonacci(n-2)


n = 8
ob = Solution()
ans = ob.fibonacci(n)

ans

'''

'''