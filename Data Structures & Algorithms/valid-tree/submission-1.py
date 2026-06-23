class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgemap = defaultdict(list)

        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)

        visited = set()

        def dfs(edge, prev):
            if edge in visited:
                return False
            
            visited.add(edge)

            for e in edgemap[edge]:
                if e != prev:
                    if not dfs(e, edge):
                        return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

                