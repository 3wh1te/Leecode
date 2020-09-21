#coding=utf-8

class Solution:
    def groupAnagrams(self, strs):
        syms = []
        res = []
        for s in strs:
            syms.append(sorted(s))

        for i,num in enumerate(syms):
            if num != " ":
                tem = [strs[i]]
                # syms.remove(num)
                for j,n in enumerate(syms):
                    if n == num and j != i:
                        tem.append(strs[j])
                        syms[j] = " "
                res.append(tem)
        return res


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
