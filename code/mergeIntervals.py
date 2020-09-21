from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x:x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                now = intervals.pop(i)
                after = intervals.pop(i)
                intervals.insert(i, [min(now[0], after[0]), max(now[1], after[1])])
            else:
                i += 1
        return intervals
if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))