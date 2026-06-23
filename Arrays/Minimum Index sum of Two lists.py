from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=float('inf')
        l=[]
        m=len(list1)
        n=len(list2)
        if(m<n):
            for x in list1:
                if x in list2:
                    if list1.index(x)+list2.index(x)==ans:
                        l.append(x)
                    elif list1.index(x)+list2.index(x)<ans:
                        l=[]
                        l.append(x)
                        ans=list1.index(x)+list2.index(x)
        else:
            for x in list2:
                if x in list1:
                    if list1.index(x)+list2.index(x)==ans:
                        l.append(x)
                    elif list1.index(x)+list2.index(x)<ans:
                        l=[]
                        l.append(x)
                        ans=list1.index(x)+list2.index(x)
        return l
                    
        
