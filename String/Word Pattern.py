class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(words)!=len(pattern):
            return False
        m1={}
        m2={}
        for c1,c2 in zip(words,pattern):
            if c1 in m1 and m1[c1]!=c2:
                return False
            if c2 in m2 and m2[c2]!=c1:
                return False
            m1[c1]=c2
            m2[c2]=c1
        return True
        