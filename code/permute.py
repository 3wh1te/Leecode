from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        in_val = nums[0]
        in_nums = self.permute(nums[1:])
        res = []
        for nums in in_nums:
            tmp = nums.copy()
            length = len(nums) + 1
            for i in range(length):
                nums.insert(i, in_val)
                res.append(nums)
                nums = tmp.copy()
        return res
if __name__ == '__main__':
    nums = [1,2,3]
    # nums.insert(3, 4)
    print(Solution().permute(nums))