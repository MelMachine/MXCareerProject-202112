# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:n+1],inorder[:n])
        root.right = self.buildTree(preorder[n+1:],inorder[n+1:])
        return root
