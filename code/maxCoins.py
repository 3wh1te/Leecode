from  typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if nums.__len__() == 1:
            return nums[0]
        max_res = 0
        for index in range(len(nums)):
            res = 0
            tem = nums.copy()
            if index == 0:
                tem.pop(index)
                res = nums[0] * nums[1] + self.maxCoins(tem)
            if index == nums.__len__() - 1:
                tem.pop(index)
                res = nums[-1] * nums[-2] + self.maxCoins(tem)
            if index > 0 and index < nums.__len__() - 1:
                res = nums[index] * nums[index + 1] * nums[index - 1] + \
                      self.maxCoins(tem[0:index + 1]) + self.maxCoins(tem[index:nums.__len__()])
            if res > max_res:
                max_res = res
        return max_res

    def maxCoins1(self, nums: List[int]) -> int:
        if nums.__len__() == 1:
            return nums[0]
        max_res = 0
        for index, num in enumerate(nums):
            tem = nums.copy()
            tem.pop(index)
            res = 0
            if index == 0:
                res = num * nums[1] + self.maxCoins(tem)
            if index == nums.__len__() - 1:
                res = num * nums[-2] + self.maxCoins(tem)
            if index > 0 and index < nums.__len__() - 1:
                res = num * nums[index + 1] * nums[index - 1] + self.maxCoins(tem)
            if res > max_res:
                max_res = res
        return max_res


if __name__ == '__main__':
    print(Solution().maxCoins([3,1,5,8]))



