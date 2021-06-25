题目：
====

(https://leetcode-cn.com/problems/climbing-stairs/submissions/)

思路：
====

爬楼梯，一共有 N 级楼梯，一次可以选择 爬一级楼梯 or 爬两级楼梯，求 爬 N 级楼梯共有多少种方式

可以知道，第 N 级楼梯的爬法只有前面 第 N - 1级楼梯和 第 N - 2级楼梯确定的。**动态规划**

**动态转移方程：**

    ans = f(n - 1) + f(n - 2)

    n == 1时，有 1 种爬楼梯方式
    n == 2时，有 2 种爬楼梯方式

但是这样的复杂度会达到 2^N， 并且超出时间限制了。

**记忆化：**

引进一个哈希表memo来记忆每次计算机的结果，查表记忆化，省略重复，复杂度可以降到 O(N)

代码：
====

```python
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution():
    memo = {}
    def climbStairs(self, n: int):
        if n == 1:return 1
        if n == 2: return 2
        
        if n in self.memo: return self.memo[n]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = ans
        return ans



# @lc code=end
```

复杂度分析：
====

- 时间复杂度：O(N)
- 空间复杂度：O(N)