class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 0
        i = 0
        while 5**i <= n:
            i += 1
        i -= 1
        for j in range(1,i + 1):
            five += int(n/5**j)
        return five
        # i = 0
        # while 2**i <= n:
        #     i += 1
        # i -= 1
        # for j in range(1,i + 1):
        #     two += int(n/2**j)
if __name__ == '__main__':
    n = 10
    print(str(n>>1))
    print(str(n))