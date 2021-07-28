剑指 Offer 26. 树的子结构
====
https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/submissions/

## 题目描述
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
```
输入：A = [1,2,3], B = [3,1]
输出：false
```
示例 2：
```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```

## 思路
DFS 遍历整棵树， 

如果有 root.val == B.val 就顺着继续往下搜， 

  - 搜到 B 这棵树为空的时候， return True
  - 如果 A 空了 or A.val != B.val return False

思路还是很简单的， 一下就能想到， 但是因为 B 这颗树 的参数判断有些麻烦， 不好传参。

所以开一个 helper() 来帮助判断找到相同节点时的树结构。

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B: return False
        
        def dfs(nodeA):
            if not nodeA: return False
            if nodeA.val == B.val:
                if self.helper(nodeA, B):
                    return True
            return dfs(nodeA.left) or dfs(nodeA.right)
        return dfs(A)
    
    def helper(self, nodeA, nodeB):
        if not nodeB: 
            return True
        if not nodeA or nodeA.val != nodeB.val:
            return False
        return self.helper(nodeA.left, nodeB.left) and self.helper(nodeA.right, nodeB.right)
```

## 复杂度分析
- 时间复杂度： O(mn) 
- 空间复杂度： O(n) 递归调用栈的深度
