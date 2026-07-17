class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # dont use default dict because it will not contain all char
        # if defaultdict is used only related chars are mapped
        # eg char contain no relation will be missing
        adj = {c : set() for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))

            # eg [abcd, abc] is wrong
            # [abc, abcd] is correct
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # w1[j] before w2[j]
                    break

        res = []

        visited = set()
        path = set()

        # dfs in reverse
        def dfs(node):
            # if a visited node is encounted again in the path then there is a cycle
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)

            for n in adj[node]:
                if not dfs(n):
                    return False
            
            res.append(node)
            
            visited.add(node)
            path.remove(node)

            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        
        return ''.join(res[::-1])



        