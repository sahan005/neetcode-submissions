class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        fresh=0

        q=deque()
        time=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while len(q)!=0 and fresh>0:
            time+=1
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    nr, nc= r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=1: #not fresh
                        continue
                    grid[nr][nc]=2
                    fresh-=1
                    q.append([nr, nc])
        
        return time if fresh==0 else -1


            

            

        
        