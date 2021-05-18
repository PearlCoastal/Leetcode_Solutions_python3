# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(array: [int]) -> TreeNode:

    def level(index: int):

        if index >= len(array) or array[index] is None:
            return None
        
        root = TreeNode(array[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        
        return root

    return level(0)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root: return None

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

root = createTree([4,7,2,6,9,1,3])


ob = Solution()
ans = ob.invertTree(root)
ans