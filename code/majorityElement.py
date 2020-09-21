class Solution:
    def majorityElement(self, nums) -> int:
        num_dict = {}
        for num in nums:
            if num_dict.get(num) == None:
                num_dict.update({num:1})
            else:
                num_dict.update({num:num_dict.get(num) + 1})
        for n in num_dict.keys():
            if num_dict.get(n) >= len(nums)/2:
                return n

if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3,1,2,2,2]))