# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head


        slow , fast, cur = head, head ,head

        totalLen = 0

        while cur:
            cur = cur.next
            totalLen += 1

        k %= totalLen

        if k == 0:
            return head

        while k > 0:
            fast = fast.next
            k -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        newHead = ListNode()
        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead

