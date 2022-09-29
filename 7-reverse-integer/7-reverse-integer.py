class Solution:
    def reverse(self, x: int) -> int:
        temp=str(x)
        string=temp[1:]
        reverse_temp=string[::-1]
        if temp[0]=='-':
            result=-1*int(reverse_temp)
            if result<-2**31:
                return 0
            else:
                return result
        else:
            result=int(temp[::-1])
            if result>2**31-1:
                return 0
            else:
                return result
        