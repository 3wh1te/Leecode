class Solution:
    def lastStoneWeight(self, stones) -> int:

        while stones.__len__() >= 2:

            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x != y:
                stones.append(y - x)
        if stones.__len__() == 1:
            return stones.pop()
        else:
            return 0


if __name__ == '__main__':
    print(Solution().lastStoneWeight([2,7,4,1,8,1]))