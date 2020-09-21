class Solution:
    def firstMissingPositive(self, nums) -> int:
        if nums == []:
            return 1
        pnums = []
        for num in set(nums):
            if num > 0:
                pnums.append(num)
        maxv = max(pnums)
        minv = min(pnums)

        if minv > 1:
            return 1
        if maxv > len(pnums):
            l = pnums
            for n in pnums:
                if n < len(pnums):
                    l[n - 1] = -1
            for index,n in enumerate(l):
                if n != -1:
                    return index + 1
        else:
            return maxv + 1

if __name__ == '__main__':
    list = [0,1,0,2,1,0,1,3,2,1,2,1,4,7,5]
    print(Solution().firstMissingPositive(list))