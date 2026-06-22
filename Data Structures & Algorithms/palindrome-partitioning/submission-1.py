class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def ispalindrome(l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def recur(l, r, curlist):
            if r > n:
                if l == n:
                    res.append(curlist)
                return
         
            # use l:r
            # print(l, r, s[l:r], s[l:r][::-1])

            # if s[l:r] == s[l:r][::-1]:
            if ispalindrome(l, r-1):
                recur(r,r+1, curlist + [s[l:r]])

            # increase r
            recur(l, r+1, curlist)

        recur(0, 1, [])
        return res



