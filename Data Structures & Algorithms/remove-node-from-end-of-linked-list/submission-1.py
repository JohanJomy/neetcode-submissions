# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ctr = self.rev(head)
        head = ctr

        prev = None
        for i in range(n-1):
            prev = ctr
            ctr = ctr.next
        
        if prev:
            prev.next = ctr.next
        else:
            head = ctr.next
        
        # return head
        return self.rev(head)
    
    def rev(self, head, prev=None):
        if head == None:
            return prev

        t = head.next
        head.next = prev
        
        return self.rev(t, head)
