class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        sign = n/abs(n)

        pows = []
        for k in range(32):
            pows.append(0)
        diff = abs(n)
        while diff != 0:
            i = 0
            m = 1
            while m <= diff:
                # double
                m = m << 1
                i += 1
            m = m >> 1
            i = i -1
            diff = diff - m
            pows[i] = 1

        res = 1
        x_ = x
        for i in pows:
            if i == 1:
                res *= x_
            x_ *= x_

        if sign == 1:
            return res
        else:
            return 1/res

if __name__ == '__main__':
    print(Solution().myPow(2.00000,13))
