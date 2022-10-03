import sys
sys.setrecursionlimit(100000)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1
            up=dfs(i-1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            down=dfs(i+1,j)
            return up and left and right and down
        
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0 and dfs(i,j)==True:
                    cnt+=1
        return cnt