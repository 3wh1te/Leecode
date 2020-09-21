from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        m1 = m2 = max(nums) + 1
        for num in nums:
            if m1 >= num:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True
        return False

    def increasingTriplet1(self, nums: List[int]) -> bool:
        forward = []
        backward = []
        length = len(nums)
        for i in range(length):
            if i == 0:
                forward.append(nums[0])
                backward.append(nums[-1])
            else:
                forward.append(max(nums[i],nums[i-1]))
                backward.append(max(nums[-i - 1],nums[-i]))
        for i in range(1,length - 1):
            if backward[- i - 1] > nums[i] and nums[i] > forward[i - 1]:
                return True
        return False

if __name__ == '__main__':
    print(Solution().increasingTriplet1([1, 2, 3, 4, 5]))
    print(Solution().increasingTriplet1([5, 4, 3, 2, 5]))


