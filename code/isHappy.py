class Solution:
    def isHappy(self, n: int) -> bool:
        res = {}
        if n == 1:
            return True
        # compute n
        while n != 1:
            res.update({n:1})
            sum = 0
            for i in str(n):
               sum += int(i)**2
            if res.get(sum):
                return False
            n = sum
        return True

if __name__ == '__main__':
    print(Solution().isHappy(68))