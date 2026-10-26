class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh_num = 0
        step = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_num += 1

        while q and fresh_num > 0:
            cur_rots = len(q)
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in q:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_num -= 1
            step += 1
        return step if fresh_num == 0 else -1
