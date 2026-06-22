"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hmap = {}

        ctr = head
        prev = None
        while ctr:
            new = Node(ctr.val)
            if prev:
                prev.next = new
            
            hmap[ctr] = new
            prev = new
            ctr = ctr.next

        if prev:
            prev.next = ctr

        ctr = head
        while ctr:
            hmap[ctr].random = hmap[ctr.random] if ctr.random else ctr.random
            ctr = ctr.next
        
        return hmap[head] if head else head

