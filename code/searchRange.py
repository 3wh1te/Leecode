from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums)
        index = -1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                index = mid
                break
        i = 0
        while (index + i) < len(nums) and nums[index + i] == nums[index]:
            i += 1
        j = 0
        while index - j >= 0 and nums[index - j] == nums[index]:
            j += 1
        return [index - j + 1, index + i - 1]



#
# if __name__ == '__main__':
#     nums = [5, 7, 7, 8, 8, 10]
#     nums = [1,3]
#     target = 1
#     print(searchRange(nums,target))