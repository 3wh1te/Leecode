from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[]]
        add_val = nums[0]
        add_nums = self.subsets(nums[1:])
        for nums in add_nums:
            res.append(nums.copy())
        for nums in add_nums:
            nums.append(add_val)
            res.append(nums)
        return res
if __name__ == '__main__':
    nums = [1,2,3]
    # nums.insert(3, 4)
    print(Solution().subsets(nums))