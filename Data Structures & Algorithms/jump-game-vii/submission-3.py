class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        q = deque([0])
        furthest = 0

        while q:
            i = q.popleft()
            for j in range(max(furthest, i+minJump), min(i + maxJump + 1, len(s))):
                # print(j)
                if s[j] == '0':
                    q.append(j)
                
                    if j == len(s) - 1:
                        return True
            
            furthest = i + maxJump
        
        return False