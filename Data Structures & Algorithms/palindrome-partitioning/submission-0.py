class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def recur(l, r, curlist):
            if r > n:
                if l == n:
                    res.append(curlist)
                return
         
            # use l:r
            print(l, r, s[l:r], s[l:r][::-1])
            if s[l:r] == s[l:r][::-1]:
                # print(l,r, 't')
                # curlist.append(s[l:r])
                recur(r,r+1, curlist + [s[l:r]])
                # curlist.pop()

            # increase r
            recur(l, r+1, curlist)

        recur(0, 1, [])
        return res

