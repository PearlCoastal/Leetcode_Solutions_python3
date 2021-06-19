# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.maxSum = float('-inf')

root = [1,2,3]
ob = Solution()
ans = ob.maxPathSum(root)

ans