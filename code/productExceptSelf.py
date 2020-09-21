from typing import List

class Solution:
    def productExceptSelf(self, nums : List[int]):
        res = []
        forward = [1]
        backword = [1]
        for i,num in enumerate(nums[0:-1]):
            forward.append(num*forward[i])
            backword.append(nums[len(nums)- i - 1]*backword[i])
        for i in range(len(nums)):
            res.append(forward[i]*backword[-i-1])
        return res

if __name__ == '__main__':
    print(Solution().productExceptSelf([2,7,4,1,8,1]))
    print(Solution().productExceptSelf([1,2,3,4]))