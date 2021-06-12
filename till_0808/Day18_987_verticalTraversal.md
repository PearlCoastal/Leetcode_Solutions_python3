- DFS
- 字典双重嵌套：key外层为列值，key内层为行值，value为list()

代码｜Python 3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        seen = defaultdict(lambda: defaultdict(list))
        
        def dfs(root, row= 0, col= 0):

            if not root:
                return

            seen[col][row].append(root.val)

            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
        
        dfs(root)
        
        res = []
        for x in sorted(seen):

            level = []
            for y in sorted(seen[x]):

                level += sorted([value for value in seen[x][y]])

            res.append(level)
        
        return res
```

复杂度分析：

- 时间复杂度： O(n)
- 空间复杂度：O(n)



