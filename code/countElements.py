class Solution:
    def countElements(self, arr) -> int:
        d = {}
        for num in arr:
            d.update({num:1})
        res = 0
        for num in arr:
            if d.get(num+1):
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().countElements([1,2,3,4,5,1,2,7]))