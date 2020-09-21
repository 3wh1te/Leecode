class Solution:
    def maxSubArray(self, nums) -> int:
        res = [nums[0]]
        for num in nums[1:]:
            if res[-1] < 0:
                res.append(num)
            else:
                res.append(num + res[-1])
        return max(res)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    