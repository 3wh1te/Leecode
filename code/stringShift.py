class Solution:
    def stringShift(self, s: str, shift) -> str:
        res_shift = 0
        for sh in shift:
            direction = sh[0] if sh[0] == 1 else -1
            res_shift += direction*sh[1]
        res_shift = res_shift % len(s)
        return s[-res_shift:] + s[0:-res_shift]

if __name__ == '__main__':
    print(Solution().stringShift('abcdefg',[[1,1],[1,1],[0,2],[1,3]]))
    print(Solution().stringShift("xqgwkiqpif", [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]))

