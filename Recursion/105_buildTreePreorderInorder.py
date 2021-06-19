# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:


        length = len(preorder)
        if not length: return None

        root = TreeNode(val= preorder[0], left= None, right= None)

        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: 1 + index], inorder[0: 1 + index])

        root.right = self.buildTree(preorder[1 + index: ], inorder[1 + index: ])

        return root