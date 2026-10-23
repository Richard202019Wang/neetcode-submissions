class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = [-c for c in count.values()]
        heapq.heapify(maxH)

        time = 0
        q = deque()
        while q or maxH:
            time += 1

            if maxH:
                c = 1 + heapq.heappop(maxH)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxH, q.popleft()[0])
        return time

