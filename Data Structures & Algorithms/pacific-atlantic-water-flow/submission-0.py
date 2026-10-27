class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited, preh):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < preh:
                return
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                dfs(dr + r, dc + c, visited, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append((r,c))
        return result
