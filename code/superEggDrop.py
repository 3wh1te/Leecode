class Solution:
    # dp + 二分
    def superEggDrop(self, K: int, N: int) -> int:
        res = []
        for i in range(K + 1):
            row = []
            for j in range(N + 1):
                if i == 0 or j == 0:
                    row.append(0)
                elif i == 1 or j == 1:
                    row.append(j)
                else:
                    min_x = j
                    left = 1
                    right = j-1
                    while left + 1 < right:
                        mid = int((left + right)/2)
                        t1,t2 = res[i-1][mid-1],row[j-mid]
                        if t1 > t2:
                            right = mid
                        elif t1 < t2:
                            left = mid
                        else:
                            right = left = mid
                            break
                    min_x = 1 + min(max(res[i - 1][k - 1], row[j - k]) for k in (left, right))
                    # for k in range(1,j):
                    #     x = max(res[i - 1][k - 1], row[j - k]) + 1
                    #     if min_x > x:
                    #        min_x = x
                    row.append(min_x)
            res.append(row)
        return res[-1][-1]

        # if K == 1 or N == 1:
        #     return N
        # min_x = N
        # for k in range(2,N):
        #    x = max(self.superEggDrop(K-1,k-1),self.superEggDrop(K,N-k)) + 1
        #    print((K,N,x,k))
        #    if min_x > x:
        #        min_x = x
        # return min_x


if __name__ == '__main__':
    print(Solution().superEggDrop(3,5000))# 32
    print(Solution().superEggDrop(1, 2)) # 2
    print(Solution().superEggDrop(2, 6)) # 3
    print(Solution().superEggDrop(3, 14)) # 4
    print(Solution().superEggDrop(3, 7807))  # 4

