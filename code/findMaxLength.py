class Solution:
    def findMaxLength(self, nums):
        flag = True
        while flag:
            flag = False
            pre = nums[0]
            pre_index = 0
            print(nums)
            i = 1
            while i < len(nums):
                num = nums[i]
                if pre > 1:
                    if num <= 1:
                        sum = 0
                        for k in nums[pre_index:i]:
                            sum = sum + k
                            nums.remove(k)
                            i -= 1
                        nums.insert(pre_index,sum)
                        i += 1
                        pre = num
                        pre_index = i
                else:
                    if num == pre:
                        pre = num
                        pre_index = i
                    elif num <= 1:
                        flag = True
                        sum = 0
                        for j in nums[pre_index: i+1]:
                            sum += j
                            nums.remove(j)
                            i -= 1
                        nums.insert(pre_index, sum + 1)
                        i += 1
                        pre = nums[i]
                        pre_index = i
                i += 1
        return max(nums)


    # 超时
    def findMaxLength1(self, nums):
        res = [0]*max(len(nums),1)
        for i in range(len(nums)):
            zero = 0
            one = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    zero += 1
                else:
                    one += 1
                if one == zero:
                    res[j] = max(res[j], j-i+1)
        return max(res)
if __name__ == '__main__':
    nums = [0,1,0,1,1,0,0,1,1,1,0,1,1,0,0]
    print(Solution().findMaxLength(nums))
