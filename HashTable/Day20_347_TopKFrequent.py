
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:

        dic = {}

        for value in nums:

            if value in dic:
                dic[value] += 1
            
            dic.setdefault(value, 1)

        #按照 value的出现次数排序
        sortDict = dict(sorted(dic.items(), key = lambda occurence: occurence[1], reverse = True))
        ans = []

        for value, occurence in sortDict.items():
            ans.append(value)
            k -= 1
            if not k: break

        '''
        #大神 精简写法

        class Solution:
            def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                d = {}
                for num in nums:
                    d[num] = d.get(num, 0) + 1
                sorted_d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
                sorted_keys = [kv[0] for kv in sorted_d]
                return sorted_keys[:k]

        '''
        
        return ans



# nums = [1,1,1,2,2,3]
# k = 2

nums = [1]
k = 1

nums = [3,0,1,0]
k = 1

ob = Solution()
ans = ob.topKFrequent(nums, k)

ans

'''
1.  不能用dict = {}

2.  sorted() 返回的是一个[( , ),( , )]

    要强制转换dict(sorted())

3.  dict中for循环

    for key, value in dict.items()

'''