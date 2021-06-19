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
    def findDuplicateSubtrees(self, root: TreeNode) -> [TreeNode]:
    
        self.ans = []
        self.traverse(root)

        return self.ans

    def traverse(self, root: TreeNode):

        record = {0: 1}
        
        if not root: return None

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        subtree = str(left) + ',' + str(right) + ',' + str(root.val)

        freq = record.get(subtree, 0)

        if freq:
            self.ans.append(root)
        
        record[subtree] += 1

        return subtree


root = createTree([1,2,3,4,None,2,4,None,None,4])
root

ob = Solution()
ans = ob.findDuplicateSubtrees(root)

ans


