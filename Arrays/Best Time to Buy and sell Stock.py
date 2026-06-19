from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mp=prices[0]
        for i in range(len(prices)):
            if prices[i]<mp:
                mp=prices[i]
            elif prices[i]-mp>profit:
                profit=prices[i]-mp
        return profit

        