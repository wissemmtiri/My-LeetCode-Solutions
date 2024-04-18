class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        res = 0

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    res += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        res -= 1
                    if row < n_rows - 1 and grid[row + 1][col] == 1:
                        res -= 1
                    if col > 0 and grid[row][col - 1] == 1:
                        res -= 1
                    if col < n_cols - 1 and grid[row][col + 1] == 1:
                        res -= 1
        return res