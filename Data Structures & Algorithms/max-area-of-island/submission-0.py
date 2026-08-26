class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        finarea=0

        def dfs(r, c, area):
            if r<0 or r>=rows or c<0 or c>= cols:
                return area
            if grid[r][c]==0:
                return area
            
            grid[r][c]=0
            area+=1

            area=dfs(r+1, c, area)
            area=dfs(r-1, c, area)
            area=dfs(r, c+1, area)
            area=dfs(r, c-1, area)

            return area

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=0
                    area=dfs(i,j, area)
                
                    finarea=max(finarea, area)
                    
        
        return finarea
        