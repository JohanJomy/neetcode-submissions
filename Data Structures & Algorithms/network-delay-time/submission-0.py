class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        size = n
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        minheap = [(0, k)] # weight, start node

        t = 0
        visited = set()
        while minheap:
            w, n = heapq.heappop(minheap)
            if n in visited:
                continue
            visited.add(n)
            t = max(t, w)

            for n1, w1 in adj[n]:
                if n1 not in visited:
                    heapq.heappush(minheap, (w+w1, n1))
                
        
        return t if len(visited) == size else -1