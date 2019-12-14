#coding=utf-8
# 超时
class Solution:
    def generateParenthesis(self, n: int):
        p = '()'
        res = []
        index = []

        n = 2*n
        for i in range(n):
            if i < n/2:
                index.append(1)
            else:
                index.append(0)

        while index[-1] < 2:
            s = ''
            for i in range(n):
                s += p[index[i]]
            res.append(s)
            col = 0
            while col < n - 1 and index[col] == 1:
                index[col] = 0
                col += 1
            index[col] += 1
            while sum(index) != n/2:
                col = 0
                while col < n - 1 and index[col] == 1:
                    index[col] = 0
                    col += 1
                index[col] += 1

        res_last = []
        for s in res:
            if self.is_vaild_parenthese(s):
                res_last.append(s)
        return res_last

    def is_vaild_parenthese(self,s: str):
        if s[0] == ')':
            return False
        stack = ''
        for ss in s:
            if ss == '(':
                stack += ss
            elif stack != '':
                stack = stack[:-1]
            else:
                stack += ss
        if stack == '':
            return True

    def valid(self,A):
        bal = 0
        for c in A:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0: return False
        return bal == 0






if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
    print(Solution().valid(')))((('))
