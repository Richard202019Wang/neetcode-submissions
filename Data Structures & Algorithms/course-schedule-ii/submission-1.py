class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_m = defaultdict(list)
        pre_num = defaultdict(int)
        for c, p in prerequisites:
            course_m[p].append(c)
            pre_num[c] += 1
        
        q = deque([i for i in range(numCourses) if pre_num[i] == 0])
        result = []
        
        while q:
            c = q.popleft()
            result.append(c)

            for p in course_m[c]:
                pre_num[p] -= 1
                if  pre_num[p] == 0:
                    q.append(p)
        
        return result if len(result) == numCourses else []


        