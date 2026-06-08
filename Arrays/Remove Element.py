class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=list(nums)
        nums.clear()
        for i in a:
            if(i!=val):
                nums.append(i)
        return len(nums)