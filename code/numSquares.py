class Solution:
    def numSquares(self, n: int) -> int:
        while n%4 == 0:
            n = int(n/4)
        res = [1]
        for i in range(2, n + 1):
            min_res = 4
            for j in range(1, int(i / 2 + 1)):
                if i == j ** 2:
                    min_res = 1
                    break
                if i > j ** 2:
                    if min_res > res[i - j**2 - 1] + 1:
                        min_res = res[i - j**2 - 1] + 1
            res.append(min_res)
        return res[-1]

    def numSquares1(self, n: int) -> int:
        if n == 1:
            return 1
        res = []
        for i in range(1,int(n/2 + 1)):
            if n == i**2:
                return 1
            if n > i**2:
                res.append(self.numSquares(n - i**2) + 1)
        return min(res)

    def numSquares2(self, n: int) -> int:
        while n % 4 == 0:
            n = int(n / 4)
        if n%8 == 7:
            return 4
        # 判断是否为1
        if int(n**0.5) ==  n**0.5:
            return 1
        # 判断是否为2
        for i in range(1, int(n/2 + 1)):
            if n - i**2 > 0:
                j = (n - i**2)**0.5
                if int(j) == j:
                    return 2
        return 3



if __name__ == '__main__':
    print(Solution().numSquares2(6665))
    print(Solution().numSquares2(12))


