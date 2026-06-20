from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        l=[]
        if len(s1)<len(s2):
            for x in s1:
                if x in s2:
                    l.append(x)
        else:
            for x in s2:
                if x in s1:
                    l.append(x)
        return l
        