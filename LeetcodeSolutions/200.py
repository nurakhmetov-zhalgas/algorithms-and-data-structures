from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = "+"
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)  # 0, 0
                    count_of_islands += 1
        return count_of_islands

    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = "+"
            while queue:
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
                        and grid[new_row][new_col] == "1"
                    ):
                        grid[new_row][new_col] = "+"
                        queue.append((new_row, new_col))

        count_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(grid, i, j)  # 0, 0
                    count_of_islands += 1
        return count_of_islands
