class Solution:
    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        start = None
        empty_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    empty_count += 1
        
        self.ans = 0
        
        def backtrack(r, c, count):
            if grid[r][c] == 2:
                if count == empty_count:
                    self.ans += 1
                return
            
            temp = grid[r][c]
            grid[r][c] = -1 
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    backtrack(nr, nc, count + 1)
            
            grid[r][c] = temp
            
        backtrack(start[0], start[1], 1)
        return self.ans