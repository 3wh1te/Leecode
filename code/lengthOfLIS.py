from typing import List
class Solution:
    # 对应长度的最小末尾
    def lengthOfLIS(self, nums: List[int]) -> int:
        min_tail = []
        def bi_find(nums, target):
            left = 0
            right = len(nums) - 1
            mid = 0
            while left < right:
                mid = int((left + right) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if target > nums[left]:
                return left + 1
            return left

        for num in nums:
            print(min_tail)
            if min_tail.__len__() == 0 or num > min_tail[-1]:
                min_tail.append(num)
            else:
                pos = bi_find(min_tail, num)
                min_tail[pos] = num
        return len(min_tail)
if __name__ == '__main__':
    print(Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))