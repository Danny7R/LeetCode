import numpy as np

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = np.array(grid).astype('bool')
        c = 1 if 1 in grid[0] else 0
        for i in range(1, len(grid)):
            overlap = np.any(np.logical_and(grid[i], grid[i-1]))
            print(overlap)
            c += 1 if (~overlap and np.any(grid[i]) == 1) else 0
        return c