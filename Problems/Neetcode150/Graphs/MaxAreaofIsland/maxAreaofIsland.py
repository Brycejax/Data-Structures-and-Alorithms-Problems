import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ans = 0
        visited = set()
        rows, columns = len(grid), len(grid[0])
        
        def bfs(i,j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))
            numOfTiles = 1
            while q:
                r , c = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if ((row in range(rows) and
                        col in range(columns) and
                        grid[row][col] == 1 and
                        (row, col) not in visited)):
                        q.append((row,col))
                        visited.add((row,col))
                        numOfTiles += 1
            return numOfTiles
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans = max(ans, bfs(i, j))
                    
        return ans