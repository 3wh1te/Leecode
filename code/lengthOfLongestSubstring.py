class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos_dict = {}
        res = []
        res_len = [0]
        for i, ss in enumerate(s):
            if i == 0:
                res.append(ss)
                res_len.append(len(ss))
            else:
                if pos_dict.get(ss) == None or (i - pos_dict.get(ss)[-1]) > len(res[-1]):
                    res.append(res[-1] + ss)
                    res_len.append(len(res[-1]))
                else:
                    res.append(s[pos_dict.get(ss)[-1] + 1:i + 1])
                    res_len.append(len(res[-1]))

            if pos_dict.get(ss):
                pos_dict.get(ss).append(i)
            else:
                pos_dict.update({ss:[i]})
        print(res)
        return max(res_len)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabds'))
    print(Solution().lengthOfLongestSubstring('bbbbbbb'))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
