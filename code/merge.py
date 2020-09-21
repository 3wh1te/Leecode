class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = []
        for i in range(m):
            n1.append(nums1[i])
        i,j = 0,0
        for k in range(m+n):
            if i < m and j < n:
                if n1[i] > nums2[j]:
                    nums1[k] = nums2[j]
                    j += 1
                else:
                    nums1[k] = n1[i]
                    i += 1
            elif i < m and j >= n:
                nums1[k] = n1[i]
                i += 1
            elif i >= m and j < n:
                nums1[k] = nums2[j]
                j += 1
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(Solution().merge(nums1, m, nums2, n))