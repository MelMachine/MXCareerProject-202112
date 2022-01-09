# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        cur = dummy = ListNode(-1)

        p = head
        

        lenNum = 0
        while p:
            p = p.next
            lenNum += 1

        p = head
        while lenNum > 0:
            smallestVal = float('inf') 
            while p and p.next:
                if p.val < smallestVal:
                    smallestVal = p.val
                cur.next = ListNode(smallestVal)

            while p and p.next:
                if p.next.val == smallestVal:
                    p.next = p.next.next
                else: 
                    p = p.next
            
            lenNum -=1

        return dummy.next


 #超时
