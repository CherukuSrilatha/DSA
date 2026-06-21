from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums1)):
            x=nums2.index(nums1[i])
            m=-1
            for j in range(x+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    m=nums2[j]
                    break
            l.append(m)
        return l

                


        