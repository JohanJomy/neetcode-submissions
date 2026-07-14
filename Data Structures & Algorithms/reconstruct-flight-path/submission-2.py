class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        tickets.sort(key=lambda x: x[1])

        for f, t in tickets:
            adj[f].append(t)
        
        # for k in adj:
        #     adj[k].sort()


        def dfs(node, cur):
            # print(cur)
            if len(cur) == len(tickets) + 1:
                return cur
            
            if not adj[node]:
                return False
            
            for i in range(len(adj[node])):
                new = adj[node].pop(i)
                res =  dfs(new, cur + [new])
                # print(res)
                if res != False:
                    # print('ture')
                    return res
                adj[node].insert(i, new)

            return False
    
        return dfs('JFK', ['JFK'])

