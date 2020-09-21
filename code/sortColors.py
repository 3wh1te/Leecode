from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = [0, 0, 0]
        for index, num in enumerate(nums):
            nums.pop(index)
            nums.insert(res[num], num)
            for i in range(num,3):
                res[i] += 1

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0, 0, 0]
        for num in nums:
            res[num] += 1

        res[1] += res[0]
        res[2] += res[1]

        for i in range(len(nums)):
            if i < res[0]:
                nums[i] = 0
            elif i < res[1]:
                nums[i] = 1
            else:
                nums[i] = 2

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)