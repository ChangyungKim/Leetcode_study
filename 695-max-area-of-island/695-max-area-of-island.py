class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global cnt
        cnt=0
        def dfs(i,j):
            global cnt
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 0
            elif grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                cnt+=1
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                return True
        cnt=0
        temp=[0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j)==True:
                    temp.append(cnt)
                    cnt=0
        return max(temp)