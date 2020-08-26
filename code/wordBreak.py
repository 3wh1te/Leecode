# 递归方法


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if len(s) == 0:
            return True
        for word in wordDict:
            if word in s:
                ss = s.split(word)
                res = True
                for seg in ss:
                    wd = wordDict.copy()
                    # wd.remove(word)
                    res = res and self.wordBreak(seg, wd)
                if res:
                    return res
            # else:
            #     wordDict.remove(word)
        return False


if __name__ == '__main__':
    # print(Solution().wordBreak('leetcode', ['leet', 'code']))
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    # print(Solution().wordBreak(s, wordDict))
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # print(Solution().wordBreak(s, wordDict))
    s = "bb"
    wordDict = ["a", "b", "bbb", "bbbb"]
    print(Solution().wordBreak(s, wordDict))
    print('bb'.split('b'))