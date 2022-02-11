# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
             
            ans.append([node.val for node in queue][-1])
            curRow = []
            for node in queue:
                if node.left:
                    curRow.append(node.left)
                if node.right:
                    curRow.append(node.right)
            queue = curRow

        return ans
