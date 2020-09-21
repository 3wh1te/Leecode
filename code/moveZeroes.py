class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i,num in enumerate(nums):
            if num == 0:
                zeros += 1
            elif zeros > 0:
                nums[i-zeros] = num
                nums[i] = 0
        print(nums)

if __name__ == '__main__':
    Solution().moveZeroes([0,1,0,3,12])
    Solution().moveZeroes([1])