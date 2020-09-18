from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices.__len__() == 0:
            return 0
        return self.maxprofit(prices, 0, -1)

    # 三种情况 是否卖 是否买 cooldown 是否为最后一个
    def maxprofit(self,prices: List[int], buy_price, flag):
        # 决定是否卖
        if flag > 0:
            temp = prices.copy()
            sell_price = temp.pop(0)
            if len(temp) == 0:
                return sell_price - buy_price
            return max(self.maxprofit(temp, 0, 0) + sell_price - buy_price,self.maxprofit(temp, buy_price, 1))
        elif flag < 0: # 是否买
            if len(prices) == 1:
                return 0
            temp = prices.copy()
            buy_price = temp.pop(0)
            return max(self.maxprofit(temp, buy_price, 1), self.maxprofit(temp, 0, -1))
        else:
            if len(prices) == 1:
                return 0
            temp = prices.copy()
            temp.pop(0)
            return self.maxprofit(temp, 0, -1)

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,0,2]))