from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        s=0
        for i in range(len(nums)):
            if(nums[i]==1):
                count+=1
                s=max(count,s)
            else:
                count=0
        return s