# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:

        inorder = sorted(preorder)

        def createBST(preorder: [int], inorder: [int]):

            if not len(preorder): return None

            root = TreeNode(preorder[0])
            index = inorder.index(root.val)

            root.left = createBST(preorder[1: index + 1], inorder[0: index + 1])
            root.right = createBST(preorder[index + 1: ], inorder[index + 1: ])

            return root
        
        return createBST(preorder, inorder)
'''

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if preorder:
            root = TreeNode(preorder[0])

            # devide = next((i for i, val in enumerate(preorder) if val > root.val), len(preorder))

            for i, val in enumerate(preorder):
                if val > root.val:
                    index = i


            root.left = self.bstFromPreorder(preorder[1: devide])
            root.right = self.bstFromPreorder(preorder[devide: ])
            return root

    

preorder = [8,5,1,7,10,12]

ob = Solution()
ans = ob.bstFromPreorder(preorder)

ans