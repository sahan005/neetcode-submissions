class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows=len(grid)
        cols=len(grid[0])
        
        visited=set()
        q=deque()

        def add(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    visited.add((i,j))
                    q.append([i,j])
        
        distance=0
        while q:
            for i in range (len(q)):
                r,c= q.popleft()
                grid[r][c]=distance
                add(r+1,c)
                add(r-1,c)
                add(r,c+1)
                add(r,c-1)
            
            distance+=1
        


        
        