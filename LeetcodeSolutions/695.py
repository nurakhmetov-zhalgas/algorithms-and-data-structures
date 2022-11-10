from collections import deque


class Solution:
    # BFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(grid, i, j):
            size = 0
            queue = deque()
            queue.append((i, j))
            grid[i][j] = -1
            while queue:
                size += 1
                row, col = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (
                        new_row < len(grid)
                        and new_col < len(grid[0])
                        and new_row >= 0
                        and new_col >= 0
                        and grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = -1
                        queue.append((new_row, new_col))
            return size

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current = bfs(grid, i, j)
                    max_area = max(max_area, current)
        return max_area

    # DFS REC
    def maxAreaOfIsland(self, grid):
        seen = set()

        def area(r, c):
            if not (
                0 <= r < len(grid)
                and 0 <= c < len(grid[0])
                and (r, c) not in seen
                and grid[r][c]
            ):
                return 0
            seen.add((r, c))
            return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c - 1) + area(r, c + 1)

        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
