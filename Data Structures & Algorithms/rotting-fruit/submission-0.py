class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        

        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    curr_row, curr_col = row + dr, col + dc
                    if (curr_row in range(rows) and curr_col in range(cols) and grid[curr_row][curr_col] == 1):
                        grid[curr_row][curr_col] = 2
                        q.append((curr_row,curr_col))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1

















        
