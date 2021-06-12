**思路：**

- 字典 dic= {数组的值：出现频率}

- sorted() + lambda 按字典中的出现频率 对字典排序

- 返回前k个值

```python
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

```

**复杂度分析：**

- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)