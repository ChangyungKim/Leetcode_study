class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=[]
        white=[]
        blue=[]
        for x in nums:
            if x==0:
                red.append(x)
            elif x==1:
                white.append(x)
            else:
                blue.append(x)
        nums[::]=red+white+blue
        return nums
        