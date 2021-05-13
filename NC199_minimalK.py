# -*- coding:utf-8 -*-

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        
        if (k > len(tinput) or len(tinput)): return 0

        tinput.sort()
        ans = [0]*k
        
        for i in range(k):
            ans[i]= tinput[i]
            
        return ans

tinput = [4,5,1,6,2,7,3,8]
k = 4

k = 8
k = 10
k = 1
k = 0
k = 2
tinput = []
k = 0

ob = Solution()
ans = ob.GetLeastNumbers_Solution(tinput, k)

ans