# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.x, self.y, self.pre = None, None, None

        def DFS(root):
            if not root:
                return 
            DFS(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root

            DFS(root.right)

        DFS(root)

        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val
