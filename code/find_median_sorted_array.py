#coding=utf-8

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 保证n > m
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 >= len2:
            l = len2
            len2 = len1
            len1 = l
            nums = nums2
            nums2 = nums1
            nums1 = nums

        s = 0
        n = len1
        m = len2

        while True:
            i = int((s + n)/2)
            j = int((m+len1+1)/2 - i)

            if i > 0 and nums1[i - 1] > nums2[j]:
                n = i - 1
            elif i < n and nums2[j - 1] > nums1[i]:
                s = i + 1
            else:
                if i == 0 or i == n:
                    if (n + m) % 2 == 1:
                        return nums2[j]
                    else:
                        return (nums2[j] + nums2[j - 1]) / 2
                if j == 0:  # 因为 n<m 所以j=0，i一定为m,且n=m 或 m-1
                    if (n + m) % 2 == 0:
                        return (nums1[m - 1] + nums2[0]) / 2
                    else:
                        return nums2[0]
                if j == m:
                    if (n + m) % 2 == 0:
                        return (nums1[0] + nums2[m - 1]) / 2
                    else:
                        return nums2[m - 1]
                if (m + n) % 2 == 1:
                    return max(nums1[i - 1], nums2[j - 1])
                else:
                    return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2




    def myFindMedianSortedArrays(self, nums1, nums2) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            l = len2
        else:
            l = len1


        if nums1 == []:
            if len(nums2) % 2 == 1:
                return nums2[int(len2 / 2)]
            else:
                return (nums2[int(len2 / 2)] + nums2[int(len2 / 2) - 1]) / 2
        if nums2 == []:
            if len(nums1) % 2 == 1:
                return nums1[int(len1 / 2)]
            else:
                return (nums1[int(len1 / 2)] + nums1[int(len1 / 2) - 1]) / 2

        # 终止条件判断
        if len1 == 1 and len2 == 1:
            return (nums1[0] + nums2[0]) / 2
        if len1 + len2 == 3:
            if len1 > len2:
                if nums1[0] < nums2[0] and nums1[1] >= nums2[0]:
                    return nums2[0]
                elif nums1[0] > nums2[0]:
                    return nums1[0]
                else:
                    return nums1[1]
            else:
                if nums1[0] < nums2[0]:
                    return nums2[0]
                elif nums1[0] > nums2[1]:
                    return nums2[1]
                else:
                    return nums1[0]
        if len1 == 2 and len2 == 2:
            if nums1[0] <= nums2[0] and nums1[1] >= nums2[1]:
                return (nums2[0] + nums2[1]) / 2
            if nums2[0] <= nums1[0] and nums2[1] >= nums1[1]:
                return (nums1[0] + nums1[1]) / 2

        # 第一个列表的中位数
        m1 = nums1[int(len1 / 2)]
        # 第二个列表的中位数
        m2 = nums2[int(len2 / 2)]

        if len1 == 1:
            if len2 % 2 == 0:
                nums2 = nums2[int(len2 / 2) - 1:int(len2 / 2) + 1]
                return self.findMedianSortedArrays(nums1, nums2)
            else:
                if m1 <= nums2[int(len2 / 2) - 1]:
                    return (nums2[int(len2 / 2) - 1] + nums2[int(len2 / 2)]) / 2
                elif m1 >= nums2[int(len2 / 2) + 1]:
                    return (nums2[int(len2 / 2) + 1] + nums2[int(len2 / 2)]) / 2
                else:
                    return (m2 + m1) / 2
        if len2 == 1:
            if len1 % 2 == 0:
                nums1 = nums1[int(len1 / 2) - 1:int(len1 / 2) + 1]
                return self.findMedianSortedArrays(nums1, nums2)
            else:
                if m2 <= nums1[int(len1 / 2) - 1]:
                    return (nums1[int(len1 / 2) - 1] + nums1[int(len1 / 2)]) / 2
                elif m2 >= nums1[int(len1 / 2) + 1]:
                    return (nums1[int(len1 / 2) + 1] + nums1[int(len1 / 2)]) / 2
                else:
                    return (m2 + m1) / 2

        if len1 == 2 and len2 > 2:
            if len2 % 2 == 0 and not (nums1[1] <= nums2[int(len2/2)-1] or nums1[0] >= nums2[int(len2/2)]):
                nums2 = nums2[int(len2 / 2) - 1:int(len2 / 2) + 1]
                return self.findMedianSortedArrays(nums1, nums2)
        if len2 == 2 and len1 > 2:
            if len1 % 2 == 0 and not (nums2[1] <= nums1[int(len1/2)-1] or nums2[0] >= nums1[int(len1/2)]):
                nums1 = nums1[int(len1 / 2) - 1:int(len1 / 2) + 1]
                return self.findMedianSortedArrays(nums1, nums2)


        if m1 > m2:
            # 可以改成三元表达式
            nums1 = nums1[0:len1 - int(l / 2)]
            nums2 = nums2[int(l / 2):]
        elif m1 == m2:
            if (len1 + len2) % 2 == 1 or (len1 % 2 == 1 and len2 % 2 == 1):
                return m1
            else:
                if nums1[int(len1 / 2) - 1] >= nums2[int(len2 / 2) - 1]:
                    return (nums1[int(len1 / 2) - 1] + m1) / 2
                else:
                    return (nums2[int(len2 / 2) - 1] + m1) / 2
        else:
            nums2 = nums2[0:len2 - int(l / 2)]
            nums1 = nums1[int(l / 2):]


        return self.findMedianSortedArrays(nums1, nums2)




if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4,5,6]
    nums1 = [1,3]
    nums2 = [2]
    s = Solution()
    print(s.findMedianSortedArrays(nums1,nums2))
