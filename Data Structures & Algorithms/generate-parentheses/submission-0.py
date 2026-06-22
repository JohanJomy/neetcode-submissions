class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opn, close, n, cur):
            if close == n:
                res.append(cur)
                return
            # print(cur)

            #open bracket
            if opn < n:
                dfs(opn + 1, close, n, cur+'(')

            #close bracket
            if opn > close:
                dfs(opn, close + 1, n, cur+')')

        dfs(0, 0, n, '')
        return res