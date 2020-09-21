class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = 1
        j = 1
        sb = 0 # S需要退格的次数
        tb = 0 # T需要退格的次数
        if len(S) > len(T):
            T = (len(S) - len(T)) * '#' + T
        else:
            S = (len(T) - len(S)) * '#' + S
        while i <= len(S) and j <= len(T):
            if S[-i] != '#' and T[-j] != '#':
                if sb == 0 and tb == 0:
                    if S[-i] != T[-j]:
                        return False
                    i += 1
                    j += 1
                if sb != 0:
                    i += 1
                    sb -= 1
                if tb != 0:
                    j += 1
                    tb -= 1
            elif S[-i] == '#' and T[-j] != '#':
                sb = sb + 1
                if tb != 0:
                    j = j + 1
                    tb -= 1
                i = i + 1
            elif S[-i] != '#' and T[-j] == '#':
                tb = tb + 1
                if sb != 0:
                    i = i + 1
                    sb -= 1
                j = j + 1
            else:
                sb += 1
                tb += 1
                j = j + 1
                i = i + 1


        if j <= len(T):
            if T[-j::-1] == (len(T) - j + 1) * '#':
                return True
            else:
                return False
        if i <= len(S):
            if S[-i::-1] == (len(S) - i + 1) * '#':
                return True
            else:
                return False
        return True






if __name__ == '__main__':
    print(Solution().backspaceCompare("ab#c","ad#c"))
    print(Solution().backspaceCompare("y#fo##f", "y#fx#o##f"))
    print(Solution().backspaceCompare("ab##c", "a#d#c"))
    print(Solution().backspaceCompare("xywrrmp", "xywrrmu#p"))

