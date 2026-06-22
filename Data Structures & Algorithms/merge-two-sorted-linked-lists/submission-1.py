# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # using a dummy first node to avoid edge cases

        dummy = ListNode()
        ctr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                ctr.next = list1
                list1 = list1.next
            else:
                ctr.next = list2
                list2 = list2.next
            
            ctr = ctr.next
        
        if list1:
            ctr.next = list1
        elif list2:
            ctr.next = list2

        return dummy.next
