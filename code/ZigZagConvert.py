# coding=utf-8

# 字符串写成z字形,找规律
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        if numRows == 1:
            return s
        for row in range(numRows):
            index = row
            while index < len(s):
                res = res + s[index]
                if row < numRows -1 and row > 0:
                    if (index + 2*numRows - 2 - 2*row) < len(s):
                        res = res + s[index + 2*numRows - 2 - 2*row]
                index = index + 2 * numRows - 2
        return res

if __name__ == '__main__':
    print(Solution().convert("A",1))