class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def bfs(i):
            if i == len(s):
                return True
                
            if i in memo:
                return memo[i]

            q = deque(wordDict)
            
            while q and i < len(s):
                w = q.popleft()

                if s[i:i+len(w)] == w:
                    print(i, w)
                    if bfs(i+len(w)):
                        memo[i] = True
                        return True
            

            memo[i] = False
            return False
        
       
        return  bfs(0)

