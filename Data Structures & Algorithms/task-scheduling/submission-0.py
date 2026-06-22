class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        countmap = defaultdict(int)
        # use minheap as maxheap
        for t in tasks:
            countmap[t] -= 1

        # countmap = Counter(tasks)
        
        maxHeap = list(countmap.values())
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append([time + n, task]) # [time available, taask value]
            
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1]) 
            
        
        return time