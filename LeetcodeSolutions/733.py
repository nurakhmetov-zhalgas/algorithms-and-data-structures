from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def dfs(image, i, j, color, start_color):
            if (
                i < 0
                or i >= len(image)
                or j < 0
                or j >= len(image[0])
                or image[i][j] != start_color
                or image[i][j] == color
            ):
                return
            image[i][j] = color
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for (dx, dy) in directions:
                ni = i + dx
                nj = j + dy
                dfs(image, ni, nj, color, start_color)

        dfs(image, sr, sc, color, image[sr][sc])
        return image
