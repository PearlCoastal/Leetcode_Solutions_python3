网易面试题 前缀和
====

## 题目描述
有一个班级有 n 个人，给出 n 个元素，第 i 个元素代表 第 i 位同学的考试成绩。

接下进行 m 次询问，每次询问给出一个数值 t ，表示第 t 个同学。

然后需要我们输出第 t 个同学的成绩超过班级百分之几的人，百分数 p 可以这样算：p = (不超过第 t 个同学分数的人数 ) / n * 100%。

输出的时候保留到小数点后 6 位，并且需要四舍五入。

输入描述：
```
第一行输入两个数 n 和 m，两个数以空格隔开，表示 n 个同学和 m 次询问。

第二行输入 n 个数值 ni，表示每个同学的分数，第三行输入 m 个数值mi，表示每次询问是询问第几个同学。

（注意，这里 2<=n，m<=100000，0<=ni<=150，1<=mi<=n）
```
输出描述：
```
输出 m 行，每一行输出一个百分数 p，代表超过班级百分之几的人。
```
示例1：

输入 ：
```
3 2
50 60 70
1 2
```
输出
```
33.333333%
66.666667%
```

## 代码
```python
import collections
class Solution:
    def f(self, scores, m):
        n = len(scores)
        arr = [0] * 151
        ans = []
        # 离散化，统计分数为 i 的有多少人
        for i in range(n):
            arr[scores[i]] += 1
        # 构造前缀和
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i - 1]
        # 模拟 m 次询问
        for i in range(len(m)):
            score = scores[m[i] - 1]
            sum = arr[score]
            ans.append(sum / n * 100)
        return ans

scores = [50, 60, 70]
m = [1, 2]

ob = Solution()
ans = ob.f(scores, m)
ans
```

## 复杂度分析

- 时间复杂度： O(m + n)
- 空间复杂度： O(1)
