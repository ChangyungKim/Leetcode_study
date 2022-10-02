class Solution(object):
    def climbStairs(self, n):
        temp=[0,1,2]
        for i in range(3,n+1):
            temp.append(temp[i-1]+temp[i-2])
        return temp[n]