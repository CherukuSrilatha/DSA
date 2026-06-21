from ast import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1="qwertyuiop"
        l2="asdfghjkl"
        l3="zxcvbnm"
        l=[]
        for word in words:
            w=word.lower()
            if all(i in l1 for i in w):
                l.append(word)
            elif all(j in l2 for j in w):
                l.append(word)
            elif all(k in l3 for k in w):
                l.append(word)
        return l


        