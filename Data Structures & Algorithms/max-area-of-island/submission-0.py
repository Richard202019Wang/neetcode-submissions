class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        max_island = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            stack = [(r, c)]
            current_island = 1
            while stack:
                current = stack.pop()
                visit.add(current)
                for dr, dc in directions:
                    cur_r, cur_c = current[0] + dr, current[1] + dc
                    if 0 <= cur_r < rows and 0 <= cur_c < cols and grid[cur_r][cur_c] == 1 and (cur_r, cur_c) not in visit:
                        visit.add((cur_r, cur_c))
                        stack.append((cur_r, cur_c))
                        current_island += 1
            return current_island



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_island = max(max_island, dfs(r, c))
        return max_island
