class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        for i in range(32,-1,-1):
            if m > 2**i and n < 2**(i+1):
                res += 2**i
                m -= 2**i
                n -= 2**i
        return res
    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        res = m
        for i in range(m+1,n+1):
            res &= i
        return res

if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd(1, 10))
    print(Solution().rangeBitwiseAnd(0, 1))
    print(Solution().rangeBitwiseAnd(1, 2147483647))
    for i in range(32,0,-1):
        print(i)