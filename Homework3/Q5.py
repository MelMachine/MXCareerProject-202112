# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        n = 0
        p = head 
        while p:
            n += 1 
            p = p.next

        x = n // k
        m =  n % k


        ans = [None] * k

        cur = head
        number = 0
        while cur:
            ans[number] = cur
            last = None

            if number < m:
                curLen = x + 1 
            else:
                curLen = x

            print(curLen)
            for i in range(curLen):
                last = cur
                cur = cur.next

            last.next = None
            number +=1

        return ans



            
        
