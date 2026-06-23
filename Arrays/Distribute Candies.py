from ast import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        s=set(candyType)
        if(n//2<=len(s)):
            return n//2
        else:
            return len(s)
        