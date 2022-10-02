class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=dict()
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]]=1
            else:
                temp[nums[i]]+=1
        for k,v in temp.items():
            if v==1:
                return k
        