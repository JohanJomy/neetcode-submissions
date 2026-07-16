class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjlist = defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                adjlist[tuple(points[i])].append([dist, tuple(points[j])])
                adjlist[tuple(points[j])].append([dist, tuple(points[i])])
        

        # Prim's
        minheap = [[0, tuple(points[0])]]
        # heapq.heapify(minheap) # (distance, point)

        visited = set()
        cost = 0

        while len(visited) < len(points):
            # print(heapq.heappop(minheap))
            c, point = heapq.heappop(minheap)
            if point in visited:
                continue
            # point = tu
            cost += c

            visited.add(point)

            for c, p in adjlist[point]:
                if p not in visited:
                    heapq.heappush(minheap, (c, p))
        
        return cost


