#coding=utf-8

# Time Limit Exceeded
def lengthOfLongestSubstring(s: str) -> int:
    max = 0
    ss = s
    length = len(s)
    for start in range(length):
        if length - start <= max:
            return max
        s = ss[start:length]
        substr = ''
        for i in range(len(s)):
            if s[i] not in substr:
                substr = substr + s[i]
                if len(substr) >= max:
                    max = len(substr)
            else:
                substr = s[i]
    return max



if __name__ == '__main__':
