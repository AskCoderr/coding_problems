class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buying_price = prices[0]
        selling_price = prices[0]
        profit = 0
        buying_price_new = None
        for i in prices[1:]:
            if buying_price_new == None:
                if i > selling_price:
                    selling_price = i
                    profit = selling_price - buying_price
                elif i < buying_price:
                    buying_price_new = i
            else:
                if (i - buying_price_new) > profit:
                    selling_price = i
                    buying_price = buying_price_new
                    buying_price_new = None
                    profit = selling_price - buying_price   
                elif i < buying_price_new:
                    buying_price_new = i                 

        return profit

print(Solution().maxProfit([4, 2, 1, 7]))

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
