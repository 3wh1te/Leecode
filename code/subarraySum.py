from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        sum_dict = {0:[0]}
        sum = 0

        for index, num in enumerate(nums):
            print(sum_dict)
            sum += num
            sums.append(sum)
            if sum_dict.get(sum) == None:
                sum_dict[sum] = [index + 1]
            else:
                sum_dict.get(sum).append(index + 1)
        print(sum_dict)
        res = 0
        for index, s in enumerate(sums):
            if sum_dict.get(s + k) != None:
                for i in sum_dict.get(s + k):
                    if i > index:
                        res += 1
        return res

if __name__ == '__main__':
    # print(Solution().subarraySum([1,1,1,1,1], 2))
    print(Solution().subarraySum([-1, -1, 1, 1], 0))

