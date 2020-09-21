class Solution:
    def titleToNumber(self, s: str) -> int:
        sheet = {}
        for i,l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            sheet[l] = i + 1
        res = 0
        for i,l in enumerate(s[::-1]):
            res += sheet.get(l) * (26**i)
        return res

if __name__ == '__main__':
    print(Solution().titleToNumber("ASUHUI"))