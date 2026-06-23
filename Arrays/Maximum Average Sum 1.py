from ast import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        ms=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            ms=max(ms,s)
        return ms/k

        