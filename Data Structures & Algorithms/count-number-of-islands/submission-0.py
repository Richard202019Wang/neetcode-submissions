class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        Row, Col = len(grid), len(grid[0])
        total_island = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nc < 0 or nr < 0 or nr >= Row or nc >= Col or grid[nr][nc] == '0':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'
        
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1":
                    bfs(r, c)
                    total_island += 1
        return total_island