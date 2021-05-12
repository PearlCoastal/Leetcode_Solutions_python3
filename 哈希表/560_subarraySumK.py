'''
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:

        result = 0
        length = len(nums)

        # time limit exceeded
        for i in range(length):
            for j in range(i, length):
                if(sum(nums[i:j+1]) == k): 
                    visible.append(nums[i:j+1])
                    result  += 1
        return result
'''

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        pre = 0
        count = 0
        dic = {0:1}

        for i in nums:

            pre += i
            if (pre-k) in dic:
                count += dic[pre-k]
            dic[pre] = dic.get(pre,0) + 1
        return count
        
# nums = [1,1,1]，k = 2
nums = [3, 4, 5, 3, 7, -2, 9]
k = 7
nums = [1,-1,0]
k = 0
nums = [1, 2, -1, 1, 1, -1, ]
k = 2

ob = Solution()
ans = ob.subarraySum(nums, k)

ans

'''
1.  dictionary:
                d = {key1 : value1, key2 : value2 }
                >>> dict = {'a': 1, 'b': 2, 'b': '3'}
                >>> dict['b']
                '3'
                >>> dict
                {'a': 1, 'b': '3'}
                >>> del dict['Name']  # 删除键是'Name'的条目

2.  dict.get(key, default=None):
                返回指定键的值，如果值不在字典中返回default值
                节省了if判断此key是否存在

3.  the sum of prefix

    pre = sum(num[0:i]) 表示当前值+所有前缀的和
    如果pre - k在字典中key存在的话，表示此子序列之和为k, 有values个
    
    字典初始状态{0：1}: 当pre-k = 0 时

4.  count += 1
    dic[pre] = 1
    👆错误的原因：当前pre-k，如果有三个以上的数的和的话，没有把结果保存下来

5.  [j...i]的子数组之和为k --> pre[i] - pre[j-1] = k --> pre[j-1] = pre[i] - k --> 以i结尾的子数组, 和为k = 统计有多少个前缀和为 pre[i] - k的 pre[j]

    在j这个位置的前缀和为pre[j-1], 从j加到i则为满足条件的子数组
    pre-k = pre[j], 如果字典中存在这个dic.get(pre-k,0), 则有 dic[pre-k]个子数组满足sum(nums[j...i]) == k

6.  dic = {前缀和pre[i]: 出现次数}
    
    pre-k
    



'''