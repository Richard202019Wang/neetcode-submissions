class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def find_surround_region():
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols -1) and board[r][c] == 'O':
                        q.append((r,c))
            while q:
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if  0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr, nc))
        find_surround_region()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = "X"
                if board[r][c] == 'T':
                    board[r][c] = "O"
        
        # def find_surround_region(ro, co):
        #     queue = deque([(ro, co)])

        #     visited = set()
        #     flag_to_change = True
        #     while queue:
        #         r, c = queue.popleft()
        #         if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
        #             flag_to_change = False

        #         visited.add((r,c))
        #         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in visited:
        #                 queue.append((nr, nc))
        #     if flag_to_change:
        #         for r, c in visited:
        #             board[r][c] = 'X'
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if not (r == 0 or r == rows - 1 or c == 0 or c == cols -1) and board[r][c] == 'O':
        #             find_surround_region(r, c)
