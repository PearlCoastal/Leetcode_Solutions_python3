目录
====
>[LC. 795 Number of Subarrays with Bounded Maximum](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md#lc-795-number-of-subarrays-with-bounded-maximum)     
>[LC. 904 Fruit into Baskets](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md#lc-904-fruit-into-baskets)     
>[LC.992 Subarrays with K Different Integers](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md#lc992-subarrays-with-k-different-integers)     
>[LC.1109 Corporate Flight Bookings](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md#lc1109-corporate-flight-bookings)       
>[LC.930 Binary Subarrays with Sum](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md#lc930-binary-subarrays-with-sum)     


LC. 795 Number of Subarrays with Bounded Maximum
====
https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum/  

    给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。    
    求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。  
    例如 :    
    输入:     
    A = [2, 1, 4, 3]   
    L = 2   
    R = 3  
    输出: 3  
    解释: 满足条件的子数组: [2], [2, 1], [3]  

## 代码
```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def atMostK(nums: List[int], k: int):
            ans = 0
            pre = 0

            for i in range(len(nums)):
                if nums[i] <= k:
                    pre += 1
                else:
                    pre = 0
                ans += pre
            return ans
        
        res = atMostK(nums, right) - atMostK(nums, left - 1)
        return res
```

LC. 904 Fruit into Baskets
====
https://leetcode-cn.com/problems/fruit-into-baskets/

    在一排树中，第 i 棵树产生 tree[i] 型的水果。
    你可以从你选择的任何树开始，然后重复执行以下步骤：
    把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
    移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
    请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
    你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
    用这个程序你能收集的水果树的最大总量是多少？
    示例 1：
    输入：[1,2,1]
    输出：3
    解释：我们可以收集 [1,2,1]。
    示例 2：
    输入：[0,1,2,2]
    输出：3
    解释：我们可以收集 [1,2,2]
    如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
    示例 3：
    输入：[1,2,3,2,2]
    输出：4
    解释：我们可以收集 [2,3,2,2]
    如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
    示例 4：
    输入：[3,3,3,1,2,1,1,2,3,3,4]
    输出：5
    解释：我们可以收集 [1,2,1,1,2]
    如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
  
## 代码
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        def atMostK(fruits: List[int], k: int):
            ans = 0
            win = collections.defaultdict(int)
            left, right = 0, 0

            for right in range(len(fruits)):
                if win[fruits[right]] == 0:
                    k -= 1
                win[fruits[right]] += 1
                while k < 0:
                    win[fruits[left]] -= 1
                    if win[fruits[left]] == 0:
                        k += 1
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        
        res = atMostK(fruits, 2)
        return res
```

LC.992 Subarrays with K Different Integers
====
https://leetcode-cn.com/problems/subarrays-with-k-different-integers/

    给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。
    （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
    返回 A 中好子数组的数目。
    示例 1：
    输入：A = [1,2,1,2,3], K = 2
    输出：7
    解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
    示例 2：
    输入：A = [1,2,1,3,4], K = 3
    输出：3
    解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
  
## 代码
```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(nums: List[int], k: int) -> int:

            if k < 0:
                return 0
            ans = 0
            left, right = 0, 0
            win = collections.defaultdict(int)
            for right in range(len(nums)):
                if win[nums[right]] == 0:
                    k -= 1
                win[nums[right]] += 1
                # sliding window is sliding...
                while k < 0:
                    win[nums[left]] -= 1
                    if win[nums[left]] == 0:
                        k += 1
                    left += 1
                ans += right - left + 1
            return ans
        
        res = atMostK(nums, k) - atMostK(nums, k - 1)
        return res
```

LC.1109 Corporate Flight Bookings 
====
https://leetcode-cn.com/problems/corporate-flight-bookings/

    这里有 n 个航班，它们分别从 1 到 n 进行编号。
    有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
    请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。
    示例 1：
    输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    输出：[10,55,45,25,25]
    解释：
    航班编号        1   2   3   4   5
    预订记录 1 ：   10  10
    预订记录 2 ：       20  20
    预订记录 3 ：       25  25  25  25
    总座位数：      10  55  45  25  25
    因此，answer = [10,55,45,25,25]
    示例 2：
    输入：bookings = [[1,2,10],[2,2,15]], n = 2
    输出：[10,25]
    解释：
    航班编号        1   2
    预订记录 1 ：   10  10
    预订记录 2 ：       15
    总座位数：      10  25
    因此，answer = [10,25]

## 代码
  
```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        ans = [0 for i in range(n + 1)]
        for left, right, k in bookings:
            ans[left - 1] += k
            if right < n:
                ans[right] -= k
        
        for i in range(n + 1):
            ans[i] += ans[i - 1]
        return ans[:-1]
```

LC.930 Binary Subarrays with Sum
====
https://leetcode-cn.com/problems/binary-subarrays-with-sum/

    给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
    子数组 是数组的一段连续部分。
    示例 1：
    输入：nums = [1,0,1,0,1], goal = 2
    输出：4
    解释：
    有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
    示例 2：
    输入：nums = [0,0,0,0,0], goal = 0
    输出：15
  
## 代码
```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atMostK(nums: List[int], goal: int):
            if goal < 0:
                return 0
            ans = 0
            left, right = 0, 0
            for right in range(len(nums)):
                goal -= nums[right]
                # sliding window is sliding...
                while goal < 0:
                    goal += nums[left]
                    left += 1
                ans += right - left + 1
            return ans
        
        res = atMostK(nums, goal) - atMostK(nums, goal - 1)
        return res
```

