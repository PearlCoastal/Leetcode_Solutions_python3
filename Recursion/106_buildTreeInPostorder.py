# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:


        length = len(inorder)
        if not length: return None

        root = TreeNode(val= postorder[-1], left= None, right= None)

        index = inorder.index(preorder[-1])

        root.left = self.buildTree(preorder[0: 1 + index], inorder[0: 1 + index])

        root.right = self.buildTree(preorder[1 + index: ], inorder[1 + index: ])

        return root