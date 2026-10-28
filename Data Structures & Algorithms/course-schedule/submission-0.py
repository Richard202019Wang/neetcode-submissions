class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        for i in range(len(prerequisites)):
            c, p = prerequisites[i]
            course_map[c].append(p)
        
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if course_map[c] == []:
                return True
            
            visited.add(c)

            for p in course_map[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            course_map[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

