# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        queue = [root]
        level = 0

        while queue:
            if level % 2 == 0:
                ins = 0
            else: ins = float("inf")

            curRow = []
            for node in queue:
                if node.val % 2 == level % 2 or level % 2 == 0 and node.val <= ins or level % 2 == 1 and node.val >= ins:
                    return False
                ins = node.val
                if node.left:
                    curRow.append(node.left)
                if node.right:
                    curRow.append(node.right)
            queue = curRow
            level += 1
        return True

        
        
