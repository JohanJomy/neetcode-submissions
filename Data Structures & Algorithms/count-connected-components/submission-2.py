class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        parent = [i for i in range(n)]

        # returns the parent of n
        def find(n):
            res = n

            while res != parent[res]:
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            # find parent of both nodes
            p1, p2 = find(n1), find(n2)

            # already merged
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2] 
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1] 
            
            return 1

        res = n
        for a, b in edges:
            res -= union(a,b)

        return res
