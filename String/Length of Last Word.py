class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=s.split(" ")
        x=""
        x=x+l[-1]
        return len(x)