class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng=0
        for i in range(len(s)):
            lst=[]
            for j in range(i, len(s)):
                if s[j] in lst:
                    break
                else:
                    lst.append(s[j])
            leng=max(leng, len(lst))
        return leng