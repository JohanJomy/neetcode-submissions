class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()

        minheap = [] # (size, end)
        
        resmap = {} # map queries size to interval

        i = 0

        for q in sorted(queries):


            while i < len(intervals) and intervals[i][0] <= q: 
                # all elements with starting val <= queries
                size = intervals[i][1] - intervals[i][0] + 1
                
                heapq.heappush(minheap, [size, intervals[i][1]])


                i += 1

            # remove all intervals not in range
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            resmap[q] = minheap[0][0] if minheap else -1
            q += 1
        
        res = []
        for i in queries:
            res.append(resmap[i])
        
        return res

