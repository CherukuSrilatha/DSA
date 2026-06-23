from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        ans=0
        for num in d:
            if num+1 in d:
                ans=max(ans,d[num]+d[num+1])
        return ans



    
        