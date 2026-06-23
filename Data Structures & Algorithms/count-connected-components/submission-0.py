class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjmap = defaultdict(list)

        for a,b in edges:
            adjmap[a].append(b)
            adjmap[b].append(a)
        
        count = 0

        visited = set()

        def dfs(v):
            if v in visited:
                return
            
            visited.add(v)

            for vv in adjmap[v]:
                dfs(vv)



        for v in range(n):
            if v not in visited:
                dfs(v)
                count += 1
        
        return count