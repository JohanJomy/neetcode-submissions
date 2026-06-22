# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        l, r = head, head
        p = dummy
        while r:
            start = l
            for i in range(k):
                if not r:
                    return dummy.next
                prev = r
                r = r.next

            end = r
            
            for i in range(k):
                t = l.next
                l.next = r
                r = l
                l = t

            p.next = r
            p = start

            # l.next = end
            l = r = end
            # print(l.val)

        return dummy.next
            

            