class Solution:
    def longestCommonPrefix(self,arr):
        arr.sort()
        first=arr[0]
        last=arr[-1]
        minlen=min(len(first),len(last))
        i=0
        while i<minlen and first[i]==last[i]:
            i+=1
        return first[:i]

