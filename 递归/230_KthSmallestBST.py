# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.rank = 0
        return self.inorder(root)

    def inorder(self, root: TreeNode):
        if not root: return None
        
        left = self.inorder(root.left)
        if left is not None: return left

        self.rank += 1
        if self.rank == self.k:
            return root.val
        
        right = self.inorder(root.right)
        if right is not None: return right     
            
