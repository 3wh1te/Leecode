#coding=utf-8

# 双指针法
# 递归会快一点
class Solution():
    def fourSum(self, nums,target):
        nums.sort()
        # res = []
        res = {}
        for i,a in enumerate(nums[:-3]):
            for j in range(i+1,len(nums) - 2):
                b = nums[j]
                left = j+1
                right = len(nums) - 1
                t = target - a -b
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    if c + d == t:
                        key = str(a) + str(b) + str(c) + str(d)
                        # 这个判断挺浪费时间的
                        if res.get(key) == None:
                            res.update({key:[a,b,c,d]})
                        # if [a,b,c,d] not in res:
                        #     res.append([a,b,c,d])
                        right -= 1
                        left += 1
                    elif c + d > t:
                        right -= 1
                    else:
                        left += 1
        return res.values()

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    # for a,b in enumerate([1, 0, -1, 0, -2, 2]):
    #     print(b)
    # print(nums[1:1])
    # print(Solution().fourSum([0, 0, 0, 0], 0))
    print(Solution().fourSum([1,0,-1,0,-2,2],0))