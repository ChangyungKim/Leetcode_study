class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer=[]
        start=0
        end=len(numbers)-1
        while True:
            if numbers[start]+numbers[end]<target:
                start+=1
            elif numbers[start]+numbers[end]>target:
                end-=1
            else:
                answer=[start+1, end+1]
                return answer