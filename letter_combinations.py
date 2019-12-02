#coding=utf-8

class Solution:
    def letterCombinations(self, digits: str):
        dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        if digits == '':
            return []
        
        nums = []
        for num in digits:
            nums.append(int(num))

        chars = []
        for num in nums:
            chars.append(dic.get(num))

        res = []
        index = []
        for _ in nums:
            index.append(0)

        while index[-1] != len(chars[-1]):
            s = ''
            for i, ss in enumerate(chars):
                s += ss[index[i]]
            print(s)
            n = 0
            while n < len(index) - 1 and index[n] == len(chars[n]) - 1:
                index[n] = 0
                n = n + 1
            index[n] += 1
            res.append(s)

        return res




if __name__ == '__main__':
    print(Solution().letterCombinations('23'))