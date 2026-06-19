
from ast import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nums=[0]*(len(gain)+1)
        nums[1]=gain[0]
        for i in range(1,len(gain)):
            nums[i+1]=nums[i]+gain[i]
        return max(nums)
