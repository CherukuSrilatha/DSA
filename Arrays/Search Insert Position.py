from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=-1
        for i in range(len(nums)):
            if nums[i]==target:
                ans=i
        if ans==-1:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
            else:
                return len(nums)

        else:
            return ans