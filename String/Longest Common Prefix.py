from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins=min(strs,key=len)
        for i in range(len(mins),0,-1):
            pre=mins[:i]
            if all(s.startswith(pre) for s in strs):
                return pre
        return ""