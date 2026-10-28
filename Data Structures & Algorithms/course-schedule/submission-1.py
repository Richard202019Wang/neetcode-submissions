class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        pre_nums = defaultdict(int)
        visited = 0

        for i in range(len(prerequisites)):
            c, p = prerequisites[i]
            adj_list[p].append(c)
            pre_nums[c] += 1
        
        q = deque([i for i in range(numCourses) if pre_nums[i] == 0])
        while q:
            c = q.popleft()
            visited += 1
            for p in adj_list[c]:
                pre_nums[p] -= 1
                if pre_nums[p] == 0:
                    q.append(p)
        
        return visited == numCourses