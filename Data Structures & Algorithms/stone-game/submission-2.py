class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # (l, r) = max alice total

        def dfs(l, r):
            if l == r:
                # last game i.e bobs turn (only one choice)
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            turn = (l-r) % 2

            if turn:
                # alice
                left = piles[l] + dfs(l+1, r)
                right = piles[r] + dfs(l, r-1)

                dp[(l, r)] = max(left, right)
            else:
                # bob playing optimaly => min for alice
                dp[(l, r)] = min(dfs(l+1, r), dfs(l, r-1))

            return dp[(l, r)]


        total = sum(piles)
        #bob = total-alice

        alice =  dfs(0, len(piles)-1)

        return alice > (total-alice)

