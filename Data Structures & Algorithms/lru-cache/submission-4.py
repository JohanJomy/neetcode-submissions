class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.ocup = 0

        self.lru.next = self.mru
        self.mru.prev = self.lru


    def get(self, key: int) -> int:
        # print('get', key, end=' ' if key in self.hmap else '\n')
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.add(self.hmap[key])
            return self.hmap[key].val
        # print('-1')
        return -1
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def add(self, node):
        node.next = self.mru
        node.prev = self.mru.prev
        self.mru.prev.next = node
        self.mru.prev = node 


    def put(self, key: int, value: int) -> None:
        if self.ocup < self.capacity and key not in self.hmap:
            node = Node(key, value)

            self.add(node)
            
            self.ocup += 1
            self.hmap[key] = node
        
        elif key not in self.hmap:
            # print(self.lru.next.key, self.hmap)
            del self.hmap[self.lru.next.key]

            self.remove(self.lru.next)
            node = Node(key, value)
            self.add(node)

            self.hmap[key] = node

        else:
            self.remove(self.hmap[key])
            self.hmap[key] = Node(key, value)
            self.add(self.hmap[key])

            

        

