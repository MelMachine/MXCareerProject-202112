# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.count = 0
        def DFS(root):
            if not root:
                return 
            DFS(root.right)
            self.count += root.val
            root.val = self.count
            DFS(root.left)

        count = 0
        DFS(root)
        return root
