**思路：**

- 字典dict = {key = nums对应的下标： value：nums}

- 一次遍历数组

- enumerate() 可以同时获得数组中的value和position

- 如果target - num在dict中的话，返回答案

- 如果不在的话，setdefault()创建新的item

```python

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:

        dict = {}

        for index, value in enumerate(nums):

            num_to_find = target - value

            if num_to_find in dict:
                position = dict[num_to_find]
                return [position, index]
            
            dict.setdefault(value)
            dict[value] = index
```

**复杂度分析：**

- 时间复杂度： O(N)
- 空间复杂度：O(N)