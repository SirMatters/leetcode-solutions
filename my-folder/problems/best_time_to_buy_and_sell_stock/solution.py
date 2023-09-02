class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        min_p = prices[0]

        for price in prices:
            if price < min_p:
                min_p = price
            else:
                res = max(res, price - min_p)
        
        return res