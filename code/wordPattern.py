class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        word_dict = {}
        pattern_dict = {}
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        for index,w in enumerate(words):
            if word_dict.get(w, -1) == -1 and pattern_dict.get(pattern[index], -1) == -1:
                word_dict[w] = pattern[index]
                pattern_dict[pattern[index]] = w
            elif word_dict.get(w) != pattern[index]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().wordPattern('abba', 'dog cat cat dog'))
    print(Solution().wordPattern('abba', 'dog cat dog dog'))
    print(Solution().wordPattern('abba', 'dog cat cat fish'))