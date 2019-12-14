#coding=utf-8
class Solution:
    def search(self, nums, target: int) -> int:
        if nums == []:
            return -1
        # find the position with bi-search
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1
        while left < right and len(nums) > 2:
            mid = int((left + right) / 2)
            if nums[mid] < nums[left]:
                right = mid
            elif mid == left:
                pos = mid
                right = left
            elif nums[mid] > nums[right]:
                left = mid
            else:
                pos = len(nums) - 1
                break
        if len(nums) == 2 and nums[0] > nums[1]:
            pos = 0
        first = nums[0]
        if target == first:
            return 0
        if target > first:
            right = pos
            left = 0
        else:
            left = pos + 1
            right = len(nums) - 1

        print((left,right))
        # use bi-search
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1

if __name__ == '__main__':
    # print(Solution().search([4,5,6,7,0,1,2],0))
    # print(Solution().search([1,2,3,4, 5, 6, 7], 0))
    print(Solution().search([1, 3], 3))
    print(Solution().search([3, 1], 1))