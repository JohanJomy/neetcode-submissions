class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        minheap = [(0, k)] # weight, start node

        t = 0
        visited = set()
        while minheap:
            w, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w)

            for n2, w1 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w+w1, n2))
                
        
        return t if len(visited) == n else -1