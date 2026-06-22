# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1

        carry = 0
        tail = head
        while l1 and l2:
            sm = l1.val + l2.val + carry

            # new = ListNode(sm%10)
            l1.val = sm%10

            carry = sm // 10

            if l1.next == None:
                tail = l1

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sm = l1.val + carry
            l1.val =  sm % 10

            carry = sm // 10
            if l1.next == None:
                tail = l1
            l1 = l1.next
        
        while l2:
            sm = l2.val + carry

            tail.next =  ListNode(sm % 10)
            tail = tail.next
            l2 = l2.next

            carry = sm // 10
        
        if carry:
            tail.next = ListNode(carry)
        
        return head
        