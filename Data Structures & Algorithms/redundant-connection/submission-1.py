class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # len(edges) = n, n-1 edges for a conected graph
        # this graph has 1 cycle so n edges

        parent = [i for i in range((len(edges)))]
        rank = [1] * len(edges)

        def find(n):
            p = n
            while p != parent[p]:
                p = parent[p]
            
            return p

        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                # p1 is parent
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return False
        
        for a, b in edges:
            if union(a-1, b-1):
                return [a, b]
