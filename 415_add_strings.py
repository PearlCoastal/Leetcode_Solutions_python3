class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1)-1, len(num2)-1
        carry = 0
        result = ""

        while( i >= 0 or j >= 0):
            
            if i >= 0: n1 = int(num1[i])
            else: n1 = 0
            if j >= 0: n2 = int(num2[j])
            else: n2 = 0
            
            temp = n1 + n2 + carry
            carry = temp // 10
            result = str(temp % 10) + result
            i -= 1
            j -= 1
        
        if(carry): return "1"+ result
        else: return result


num1 = "12345"
num2 = "935"

ob = Solution()
ans = ob.addStrings(num1, num2)

ans