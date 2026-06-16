class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        
        max_area = 0
        def dfs(r, c):
            nonlocal local_area
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return
            
            grid[r][c] = 0
            local_area += 1

            for dr, dc in directions:
                dfs(r + dr, c + dc)
                

        for r in range(rows):
            for c in range(cols):
                local_area = 0
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, local_area)

        return max_area