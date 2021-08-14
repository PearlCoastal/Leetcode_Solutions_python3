剑指 Offer 32 - III. 从上到下打印二叉树 III
====
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/

## 题目描述
<img width="722" alt="截屏0003-08-14 16 18 30" src="https://user-images.githubusercontent.com/10908630/129439416-4effb923-7539-4467-99f5-a7a99b5d7693.png">

## 思路
指路 👉 [[32-II] 从上到下打印二叉树 II](https://github.com/PearlCoastal/Leetcode_Solutions_python3/blob/master/%E5%89%91%E6%8C%87offer/32-i.md)

好家伙， 按层打包已经满足不了他了， 还要走之字型。

这道题在 [32-II] 的基础上增加了一次奇偶层判断。

1. 奇数层从左到右输出， 偶数层从右到左输出。

  如何判断当前层是奇数层还是偶数层呢， 其实看结果列表 ans 就可以了。

  ans 的长度就是已经遍历过的层数。 ans 对 2 取余就可以知道当前层是奇数层还是偶数层了。

2. 奇偶层判断完了， 接下来就是如何实现偶数层从右往左输出了。

   用来暂时保存当前层节点值的 level 列表
   
   - 偶数层： 新的值加入不从尾部加入， 采用头插法就可以实现从右往左输出了。
   
   - 奇数层： 就还照样 append 从尾部插入就可以了。
   


## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                cur = queue.popleft()
                if len(ans) % 2:
                    level.appendleft(cur.val)
                else:
                    level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            ans.append(list(level))
        return ans
```

## 复杂度分析
- 时间复杂度： O(n)
- 空间复杂度： O(n)
