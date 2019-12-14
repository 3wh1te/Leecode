# coding=utf-8

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = (1, s[0:1])  # 维护最长回文
        for i in range(len(s)):
            st = s[i]
            for j in range(i + p[0], len(s)):
                if st == s[j] and self.isPalindrome(s[i:j + 1]):
                    p = (j - i + 1, s[i:j + 1])
        return p[1]

    def isPalindrome(self, s: str):
        if s == s[::-1]:
            return True
        else:
            return False


