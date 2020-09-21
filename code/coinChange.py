from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        v_dict = {amount:1}
        i = 0
        while v_dict.__len__() != 0:
            i = i + 1
            new_dict = {}
            for value in v_dict:
                for coin in coins:
                    if value - coin == 0:
                        return i
                    if value - coin > 0:
                        new_dict[value - coin] = 1
            v_dict = new_dict
        return -1



    def coinChange1(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = amount + 1
        for coin in coins:
            tmp = self.coinChange1(coins,amount - coin)
            if tmp < res and tmp != -1:
                res = tmp
        if res != amount + 1:
            return res + 1
        else:
            return -1
if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 1111))
    # print(Solution().coinChange1([1, 2, 5], 100))#
    dict = {}
    dict[1] = 2
    print(dict.items()[0])
