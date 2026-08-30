class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 1000000
        maxx = -100000

        for price in prices:
            if price < minn:
                minn = price
            gain = price - minn
            if gain > maxx:
                maxx = gain
        
        if maxx <= 0:
            return 0
        return maxx
            


        