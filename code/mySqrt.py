import math
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = int((start + end) / 2)
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid - 1
            else:
                start = mid + 1
        return start - 1

    def mySqrt1(self, x: int) -> int:
        return int(math.sqrt(x))

if __name__ == '__main__':
    print(Solution().mySqrt(24))