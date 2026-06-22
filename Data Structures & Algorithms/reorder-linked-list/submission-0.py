# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        # (odd length)
        if f:
            s = s.next
        
        p = None
        while s:
            n = s.next
            s.next = p
            p = s
            s = n
        
        first = head
        last = p
        while last:
            t_l = last.next
            t_f = first.next

            first.next = last
            last.next = t_f
        
            first = t_f
            last = t_l
        
        first.next = None
        