LC. 347 Top K Frequent Elements
====
https://leetcode-cn.com/problems/top-k-frequent-elements/

	给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
	示例 1:
	输入: nums = [1,1,1,2,2,3], k = 2
	输出: [1,2]
	示例 2:
	输入: nums = [1], k = 1
	输出: [1]
	
> [实现最小堆](https://github.com/PearlCoastal/Leetcode_GitOn/new/master#%E6%89%8B%E5%86%99%E6%9C%80%E5%B0%8F%E5%A0%86)	<br>
> [Top K	最小堆解法](https://github.com/PearlCoastal/Leetcode_GitOn/new/master#top-k-%E6%9C%80%E5%B0%8F%E5%A0%86%E8%A7%A3%E9%A2%98)		<br>
> [Top K 字典解法](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day20_347_TopKFrequent.md)

手写最小堆
====
## 思路

堆的核心： 动态求极值。

适合求解最大值最小值的题目。

小顶堆： 父节点的值不大于儿子的值 = 根节点就是最小值 --> 求最大的几个数

大顶堆： 父节点的值不小于儿子的值 = 根节点就是最大值 --> 求最小的几个数

先上一个手写最小堆的代码， 上浮 和 下沉 操作， 了解了之后在写代码， 其实还蛮简单的。

而且很有趣 ٩(˃̶͈̀௰˂̶͈́)و

## 出堆

根节点 和 尾节点 交换， pop 根节点 = 此时的尾节点

然后对此时堆的顶点进行`下沉`操作。

交换过后的节点一定是不满足堆的性质的。

所以从`堆顶`开始， 根节点 和 `较小的节点` 交换， 重复此操作， 直到得到正确的堆。

## 入堆

新节点从堆的`尾部`插入， 然后`上浮`到正确位置。

由于小顶堆的每个子节点一定比父节点小， 所以上浮操作的时候， 只要考虑`父节点`和本身的大小关系就可以了。

如果大于父节点， 就交换位置， 重复此操作， 直到得到正确的堆。

## 堆的性质

下沉操作和堆的高度有关， 时间复杂度O(h)， h 为树高。

二叉堆是一颗完全二叉树， 所以树高大约是 logN， N 为节点个数。

## 代码 实现最小堆

```python
class min_heap:
    def __init__(self, A = []):
        self.heapify(A)
    
    def heapify(self, A):
        self.h = [0] + A
        i = 1
        while i < len(self.h):
            self.shift_down(i)
            i = i + 1

    def shift_up(self, i):
        while i // 2 > 0:
            if self.h[i] < self.h[i//2]:
                self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i = i // 2

    def shift_down(self, i):
        while (i * 2) <= len(self.h) - 1:
            min_child = self.minChild(i)
            if self.h[i] > self.h[min_child]:
                self.h[i], self.h[min_child] = self.h[min_child], self.h[i]
            i = min_child
    
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.h) - 1:
            return left_child
        if self.h[left_child] < self.h[right_child]:
            return left_child
        else:
            return right_child
        

    def heappop(self):
        if len(self.h) == 1:
            return None
        pop_node = self.h[1]
        self.h[1] = self.h[len(self.h) - 1]
        self.h.pop()
        self.shift_down(1)
        return pop_node

    def heappush(self, a):
        self.h.append(a)
        self.shift_up(len(self.h) - 1)

h = min_heap([8,3,4,5,2])
```
Top K 最小堆解题
====
## 思路
然后来解这道题， 题目要求出现频率前 k 高的数组元素， 偷了个懒用了 Counter() 求出现频率啦 ⁄(⁄ ⁄ ⁄ω⁄ ⁄ ⁄)⁄ 

利用 heapq 建立一个小顶堆， 然后遍历「出现次数数组」 dic：

- 如果堆的元素个数小于 k，就可以直接插入堆中。

- 如果堆的元素个数等于 k， 有新元素要入堆，则检查 堆顶元素 与 新元素 出现次数的大小。
	
	如果堆顶元素的出现频率更大，说明至少有 k 个数字的出现次数比当前值大，故舍弃新元素
	
	否则，将堆顶元素出堆，并将新元素入堆。
	
	遍历完成后，堆中的元素就代表了「出现次数数组」中前 k 大的值。
	
## 代码
```python
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:

        dic = Counter(nums)
        h = []
        for num, freq in dic.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            else:
                if freq > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (freq, num))
        return [x[1] for x in h]
```

## 复杂度分析
Counter() 遍历数组求出现频率的复杂度 O(N)； k 为最小堆中节点的个数， 堆插入删除操作的复杂度 O(logK)
哈希表的大小 O(N), 堆大小 O（K）

- 时间复杂度： O（Nlogk）
- 空间复杂度： O(N)

手写建立最小堆 
====

建立一个固定大小为 k 的 最小堆。

然后维持堆大小的情况下， 遍历出现频率数组。

呜呜呜呜， 我太厉害了， 我能手写 最小堆了。

。・゜・(ノД`)・゜・。

```python
import collections
class Solution:
    
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        dic = collections.Counter(nums)
        dic = list(dic.items())
        self.k = k
        self.h = [(0, 0)]

        for i in range(len(dic)):
            if len(self.h) < self.k + 1:
                self.heappush(dic[i])
            else:
                if dic[i][1] > self.h[1][1]:
                    self.heappop()
                    self.heappush(dic[i])
        
        return [x[0] for x in self.h[1:]]

    def heappush(self, a):
        self.h.append(a)
        self.shift_up(len(self.h) - 1)

    def heappop(self):
        if len(self.h) == 1:
            return None
        self.h[1] = self.h[(len(self.h) - 1)]
        self.h.pop()
        self.shift_down(1)
        #return pop_node

    def shift_up(self, i):
        while i // 2 > 0:
            if self.h[i][1] < self.h[i//2][1]:
                self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i = i // 2

    def shift_down(self, i):
        while (i * 2) < self.k:
            min_child = self.minChild(i)
            if self.h[i][1] > self.h[min_child][1]:
                self.h[i], self.h[min_child] = self.h[min_child], self.h[i]
            i = min_child
        
    def minChild(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if right_child > len(self.h) - 1:
            return left_child
        if self.h[left_child][1] < self.h[right_child][1]:
            return left_child
        else:
            return right_child
```

## 哈希表

```python
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        ans = []
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        sort_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
        
        for i in range(k):
            ans.append(sort_dic[i][0]) 
        return ans
```
