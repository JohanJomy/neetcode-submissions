class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []

        for p in points:
            distance.append([p[0]**2 + p[1]**2, p[0], p[1]])
        
        heapq.heapify(distance)

        res = []
        for i in range(k):
            res.append(heapq.heappop(distance)[1:])

        return res
