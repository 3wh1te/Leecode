class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i,ss in enumerate(s[::-1]):
            # print(stack)
            if ss == '*':
                star.append(i)
            elif ss == '(' and stack.__len__() >= 1:
                stack.pop()
            elif ss == '(' and star.__len__() > 0:
                star.pop()
            elif ss == ')':
                stack.append(i)
            else:
                return False
        while stack.__len__() > 0 and star.__len__() > 0:
            if stack[-1] > star[-1]:
                return False
            stack.pop()
            star.pop()
        if stack.__len__() > 0:
            return False
        else:
            return True
if __name__ == '__main__':
    print(Solution().checkValidString('(*))'))
    print(Solution().checkValidString(')('))
    print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
    print(Solution().checkValidString('(()(*)()'))
    print(Solution().checkValidString('(())*)()'))
