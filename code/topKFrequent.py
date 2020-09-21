from typing import List
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        fres = collections.Counter(nums)

        for fre in fres.most_common(k):
            res.append(fre[0])
        return res
# if __name__ == '__main__':
