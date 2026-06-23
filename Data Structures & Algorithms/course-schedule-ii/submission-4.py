class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqmap = defaultdict(list)

        for a,b in prerequisites:
            prereqmap[a].append(b)
        
        visited = set()

        res = []
        resset = set()
        dp = [0] * numCourses

        def dfs(course):
            if course in visited:
                return False
            
            if dp[course]:
                return True

            visited.add(course)
            for c in prereqmap[course]:
                if not dfs(c):
                    return False

            visited.remove(course)
            dp[course] = 1
            # if course not in resset:
            #     resset.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if c not in prereqmap:
                res.append(c)
                continue

            if not dfs(c):
                return []
        
            # if c not in res:
                

        return res
