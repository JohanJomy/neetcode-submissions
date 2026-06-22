class MedianFinder:

    def __init__(self):
        self.maxheap = [] # with first half (-ve values)
        self.minheap = [] # with 2nd half
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.maxheap, -num)
        
        if self.minheap and self.maxheap and -self.maxheap[0] > self.minheap[0]:
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n)
        
        while len(self.maxheap) > len(self.minheap) + 1:
            n = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -n) #make it +ve
        
        while len(self.minheap) > len(self.maxheap) + 1:
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n) #make it +ve
        
        print(self.maxheap, self.minheap)

        

    def findMedian(self) -> float:

        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        return -self.maxheap[0]
        
        