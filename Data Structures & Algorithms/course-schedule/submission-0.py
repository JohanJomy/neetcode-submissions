class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqmap = defaultdict(list)

        for a, b in prerequisites:
            prereqmap[a].append(b)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for c in prereqmap[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            return True

        for course in range(numCourses):
            if course not in prereqmap:
                continue
            if not dfs(course):
                return False
        
        return True
            