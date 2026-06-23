from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1=len(mat)
        c1=len(mat[0])
        if r*c!=r1*c1:
            return mat
        l=[]
        for i in range(r1):
            for j in range(c1):
                l.append(mat[i][j])
        res=[]
        k=0
        for i in range(r):
            l2=[]
            for j in range(c):
                l2.append(l[k])
                k+=1
            res.append(l2)
        return res
                

        