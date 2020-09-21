from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res = [1]
        min_res = [1]
        for i in nums:
            if i > 0:
                max_res.append(i * max(1, max_res[-1]))
                min_res.append(i * min(1, min_res[-1]))
            else:
                max_res.append(i * min(1, min_res[-1]))
                min_res.append(i * max(1, max_res[-2]))
        return max(max_res[1:])
