# coding=utf-8


class Solution:
    def intToRoman(self, num: int) -> str:
        sym = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

        res = ''
        for value in [1000,100,10,1]:
            remainder = int(num / value)
            if remainder < 4 or value == 1000:
                res += remainder * sym.get(value)
            elif remainder == 4:
                res += sym.get(value) + sym.get(5 * value)
            elif remainder < 9:
                res += sym.get(5*value) + (remainder - 5)*sym.get(value)
            else:
                res += sym.get(value) + sym.get(value*10)
            num = num%value
        return res




if __name__ == '__main__':
    print(Solution().intToRoman(1994))