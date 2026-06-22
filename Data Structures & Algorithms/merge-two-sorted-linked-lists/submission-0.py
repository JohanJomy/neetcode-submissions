# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
            
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        ctr = head
        print(ctr.val)
        while list1 and list2:
            if list1.val <= list2.val:
                # print(list1.val)
                ctr.next = list1
                ctr = list1
                list1 = list1.next
            else:
                # print(list2.val)
                ctr.next = list2
                ctr = list2
                list2 = list2.next
        
        if list1:
            ctr.next = list1
        elif list2:
            ctr.next = list2
        
        ctr = head
        while ctr:
            print(ctr.val)
            ctr = ctr.next
        
        return head

        
        


