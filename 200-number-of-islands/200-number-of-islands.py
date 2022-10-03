class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            elif grid[i][j]=='0':
                return False
            else:
                grid[i][j]='0'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                return True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if dfs(i,j)==True:
                    cnt+=1
        return cnt
                