# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur = dummy = ListNode(0)

        carry = 0

        while l1 or l2:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0

            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0

            total = n1 + n2 + carry

            carry = total //10

            cur.next = ListNode(total % 10)

            cur = cur.next



        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next
