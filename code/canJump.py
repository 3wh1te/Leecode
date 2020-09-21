from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for index in range(len(nums)):
            if target <= nums[len(nums) - index - 1] + len(nums) - index - 1:
                target = len(nums) - index - 1
        if target == 0:
            return True
        else:
            return False

    def canJump1(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            for i in range(nums[0]):
                if self.canJump(nums[nums[0] - i:]):
                    return True
            return False

