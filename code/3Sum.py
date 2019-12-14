#coding=utf-8


class Solution:
    # 超时版本
    def threeSum(self, nums):
        res = []
        for a in nums:
            b_nums = nums[:]
            b_nums.remove(a)
            for b in b_nums:
                c_nums = b_nums[:]
                c_nums.remove(b)
                hash_ = {}
                for i in range(len(c_nums)):
                    if hash_.get(c_nums[i]):
                        # 如果存在hash，那么就存储进去
                        hash_[c_nums[i]].append(i)
                    else:
                        hash_[c_nums[i]] = [i]
                c = -a - b
                if hash_.get(c):
                    tem = [a, b, c]
                    tem.sort()
                    if tem not in res:
                        res.append(tem)
        return res





if __name__ == '__main__':
    res = Solution().threeSum([3,0,-2,-1,1,2])
    print(res)