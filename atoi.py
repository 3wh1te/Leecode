# coding=utf-8

class Solution:
    # 不考虑e和.的情况,只考虑 + -
    def myAtoi(self, str: str) -> int:
        # 去字符串前面的空格
        i = 0
        s = str[i]
        while s == " " and (i + 1) < len(str):
            i = i + 1
            s = str[i]
        str = str[i:]
        if len(str) == 0:
            return 0

        str = str.split('e')[0]
        num = ''
        for i in range(len(str)):
            try:
                num = float(str[0:i+1])
            except Exception as e:
                pass


        if num == '':
            return 0

        num = int(num)

        # num = str[0]
        # num = str
        # for s in str[1:]:
        #     if s not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        #         num = str.split(s)[0]
        #         break

        # print(num)
        # try:
        #     num = float(num)
        # except Exception as e:
        #     return 0
        if num >= 2 ** 31 - 1:
            num = 2 ** 31 - 1
        if num <= -2 ** 31:
            num = -2 ** 31
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("   -115579378e25"))