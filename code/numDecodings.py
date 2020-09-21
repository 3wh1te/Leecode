class Solution:
    def numDecodings(self, s: str) -> int:
        index = 0
        length = len(s)
        while index < length and s[index] == '0':
                index += 1
        res = [0]
        length -= index
        index = 0
        while index < length:
            if index > 1:
                if int(s[index-1: index+1]) <= 26 and int(s[index-1: index+1]) >= 10:
                    res.append(res[-1] + res[-2])
                else:
                    res.append(res[-1])
            elif index == 0:
                res.append(1)
            else:
                if int(s[index-1: index+1]) <= 26:
                    res.append(2)
                else:
                    res.append(1)
            index += 1
        return res[-1]

if __name__ == '__main__':
    print(Solution().numDecodings('012'))
    print(Solution().numDecodings('120'))
