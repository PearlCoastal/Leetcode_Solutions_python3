
from collections import defaultdict
class Solution():
    def minSubarray(self, nums: [int], k: int) -> int:

        total = sum(nums)
        if total < k: return -1
        target = total % k

        if not target: return 0

        #ans初始化为数组长度，最大值
        pre, ans = 0, len(nums)

        dic = defaultdict(int)
        #子数组从第一个数开始取值，比如第一个数到第七位数，但是数组下标是从0开始，就是0...6，只有(6-0)个数，所以dic[0]初始化为-1的话，就是正确的(6-(-1))=7个数
        dic = {0: -1}

        for index, element in enumerate(nums):
            pre += element

            #历史前缀和模k的值 保存到哈希表中
            dic[pre % k] = index

            if (pre - total) % k in dic:
                #如果存在几个位置同余的话，删除最短的子串
                ans = min(ans, index - dic[(pre - total) % k])
            
        #如果ans == len(nums)代表把整个数组全部删掉，题目要求是返回-1
        return ans if ans != len(nums) else -1

nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
k = 148

ob = Solution()
ans = ob.minSubarray(nums, k)
ans