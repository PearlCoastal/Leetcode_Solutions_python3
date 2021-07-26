import bisect
class Solution:
    def minOperations(self, target: [int], arr: [int]) -> int:

        m, n = len(target), len(arr)
        dic = {}
        for i, num in enumerate(target):
            dic[num] = i
        LIS = []
        for num in arr:
            if num in dic:
                if not LIS or LIS[-1] < dic[num]:
                    LIS.append(dic[num])
                else:
                    i = bisect.bisect_left(LIS, dic[num])
                    LIS[i] = dic[num]
        return m - len(LIS)

target = [5,1,3]
arr = [9,4,2,3,4]

target = [6,4,8,1,3,2]
arr = [4,7,6,2,3,8,6,1]


ob = Solution()
ans = ob.minOperations(target, arr)
ans