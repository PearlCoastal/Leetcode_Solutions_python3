# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'None'

        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(dataset):
            val = dataset.pop(0)
            
            if val == 'None': return None

            root = TreeNode(int(val))
            root.left = dfs(dataset)
            root.right = dfs(dataset)
            
            return root

        dataset = data.split(',')
        
        return dfs(dataset)


