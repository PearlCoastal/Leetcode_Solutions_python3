class Solution:
    def generateParenthesis(self, n: int) -> [str]:

        ans = []
        
        def generate(A: [str]) -> [str]:

            if len(A) == 2*n:
                if valid(A):
                    # ans.append("".join(A))
                    ans.append(A)

            else:
                A.append('(')
                generate(A)
                A.pop()

                A.append(')')
                generate(A)
                A.pop()
        
        def valid(A: []) -> bool:
            balance = 0

            for i in A:

                if i == '(':
                    balance += 1
                else:
                    balance -= 1
            
                if balance < 0: return False
            
            if balance == 0: return True
            else: return False
            
        generate([])
        return ans

n = 3

ob = Solution()
ans = ob.generateParenthesis(n)

ans