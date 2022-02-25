# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if not root:
                return 0, 0
            stealLift, noLeft = recur(root.left)
            stealRight, noRight = recur(root.right)

            return root.val + noLeft + noRight, max(stealLift, noLeft) + max(stealRight, noRight)
        return max(recur(root))
