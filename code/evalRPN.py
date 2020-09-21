from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        while tokens.__len__() != 0:
            op = tokens.pop(0)

            if op == '+':
                res.append(res.pop(-1) + res.pop(-1))
            elif op == '-':
                res.append(res.pop(-2) - res.pop(-1))
            elif op == '*':
                res.append(res.pop(-1) * res.pop(-1))
            elif op == '/':
                res.append(int(res.pop(-2) / res.pop(-1)))
            else:
                res.append(int(op))
        return res[0]
if __name__ == '__main__':
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))