class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        old_numerators = {}
        res += str(int(numerator/denominator))
        if numerator % denominator == 0:
            return res
        res += '.'
        numerator = (numerator % denominator) * 10
        index = len(res)
        while numerator != 0 and old_numerators.get(numerator, -1) == -1:
            old_numerators[numerator] = index
            res += str(int(numerator / denominator))
            index += 1
            if numerator < denominator:
                numerator *= 10
            else:
                numerator = (numerator % denominator) * 10

        if numerator == 0:
            return res
        index = old_numerators.get(numerator)
        end = len(res) - 1
        while res[end] == '0':
            end -= 1
        return res[0:index] + '(' + res[index:end + 1] + ')'
if __name__ == '__main__':
    print(Solution().fractionToDecimal(1, 2))
    print(Solution().fractionToDecimal(1, 3))
    print(Solution().fractionToDecimal(2, 3))
    print(Solution().fractionToDecimal(2, 1))
    print(Solution().fractionToDecimal(4, 333))
    print(Solution().fractionToDecimal(-2147483648,1))
    print(Solution().fractionToDecimal(-50, 8))
