"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head
        
        p = head
        while p:
            newNode = Node(p.val,None,None)
            newNode.next = p.next
            p.next = newNode
            p = newNode.next

        p = head

        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next 

        p = head
        cur = dummy = Node(-1,None,None)

        while p :
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next

        return dummy.next
        
