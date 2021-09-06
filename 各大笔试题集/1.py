class Solution:
    def median(self , arr ):
        # write code here

        arr.sort()
        index = len(arr) // 2
        return arr[index]

arr = [1.00000,3.00000,2.00000]

ob = Solution()
ans = ob.median(arr)

ans