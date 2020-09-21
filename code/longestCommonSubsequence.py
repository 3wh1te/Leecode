class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                if i == 0 and j == 0:
                    if text1[i] == text2[j]:
                        row.append(1)
                    else:
                        row.append(0)
                elif i == 0 and j != 0:
                    if text1[i] == text2[j]:
                        row.append(1)
                    else:
                        row.append(row[-1])
                elif i != 0 and j == 0:
                    if text1[i] == text2[j]:
                        row.append(1)
                    else:
                        row.append(res[-1][j])
                else:
                    if text1[i] == text2[j]:
                        row.append(res[-1][j - 1] + 1)
                    else:
                        row.append(max(res[-1][j], row[j - 1]))
            res.append(row)
        return res[-1][-1]

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            return self.longestCommonSubsequence(text1[1:], text2[1:]) + 1
        else:
            return max(self.longestCommonSubsequence(text1[1:], text2), self.longestCommonSubsequence(text1,text2[1:]))
if __name__ == '__main__':
    print(Solution().longestCommonSubsequence('abcde', 'ace'))