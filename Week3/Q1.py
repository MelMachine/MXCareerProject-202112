# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """


        cur = dummy  = ListNode(0,head)


        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else: 
                

                cur = cur.next

        return dummy.next
