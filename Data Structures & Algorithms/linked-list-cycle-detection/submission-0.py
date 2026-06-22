# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = s = head

        while f:
            s = s.next
            if f.next:
                f = f.next.next
            else:
                break
            if s == f:
                return True

        return False