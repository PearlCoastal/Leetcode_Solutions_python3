#题目：

    You are given a list of positive integers nums and an integer target. Consider an operation where we remove a number v from either the front or the back of nums and decrement target by v.

    Return the minimum number of operations required to decrement target to zero. If it's not possible, return -1.

    Constraints:    n ≤ 100,000 where n is the length of nums
    
    Example 1:  Input nums = [3, 1, 1, 2, 5, 1, 1] target = 7 Output 3 Explanation We can remove 1, 1 and 5 from the back to decrement target to zero.

    Example 2:  Input nums = [2, 4] target = 7 Output -1 Explanation There's no way to decrement target = 7 to zero.

---
**思路：**

题目要求是从给定数组的 **头尾** remove element，make sum(remove element) == target, 返回 **最小**移除次数
sum(remove element) = target 转换 --> 留下的数组之和  = sum(A) - target, 而留下的数组为连续数组
所以题目转换成：求一个**连续**子数组 和为 sum(A) - target，最小移除次数 = **最长子数组**

- 滑动窗口：涉及到头尾元素，并且最后留下的是**连续**数组元素
    slow:  滑动窗口左侧
    fast:  滑动窗口右侧
    cur:   保存当前窗口元素之和

```python
class Solution:
    def solve(self, A, target):
        if not A and not target: return 0

        #ans 初始值设置为最大，如果全部移除都不等于target的话，就return -1
        ans = float('inf')
        stay = sum(A) - target
        #当前子数组之和
        cur = 0
        #滑动窗口左右两端索引
        slow, fast = 0,0
        for fast in range(len(A)):
            cur += A[fast]
            #当前窗口之和 > target，收缩左边界
            while slow <= fast and cur > target:
                cur -= A[slow]
                slow += 1
            if cur == stay:
                #最小移除次数 = min(数组长度 - 当前子数组长度)
                #当前子数组长度： fast - slow + 1
                ans = min(ans, len(A) - (fast - slow + 1))
        return -1 if ans == float('inf') else ans          
```
**复杂度分析：**
- 时间复杂度：O(N)
- 空间复杂度：O(1)

---
- 双指针：左边+右边 是否 = target

```python
class Solution:
    def solve(self, nums, target):
        if not nums:
            return 0 if target == 0 else -1

        if sum(nums) < target:
            return -1
        
        left = 0
        left_sum = 0
        #先从左边开始加，直到找到大于等于target的数停止
        while left < len(nums) and left_sum < target:
            left_sum += nums[left]
            left += 1
        #只找左边，找到了的情况
        ans = left if left_sum == target else float('inf')

        right = len(nums)
        right_sum = 0

        #停止条件，左边没有元素
        while left > 0:
            left -= 1
            #挨个删除左边最右边的值
            left_sum -= nums[left]

            while right >= left and left_sum + right_sum < target:
                right -= 1
                #挨个加入右边的元素
                right_sum += nums[right]
            
            if left_sum + right_sum == target:
                #如何计算长度
                ans = min(ans, left + len(nums) - right)
            
        return ans if ans != float('inf') else -1

```
---

- 能力检测二分：

```python
if not A and not target: return 0

        def possible(mid: int) -> bool:

            

        left, right = 0, len(A)
        ans = len(A) + 1

        while left <= right:
            mid = (left + right) // 2

            if possible(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return -1 if ans == len(A) + 1 else ans
```            
