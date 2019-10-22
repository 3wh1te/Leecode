#coding=utf-8

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    
    len1 = len(nums1)
    len2 = len(nums2)
    # 终止条件判断
    if len1 == 1 and len2 == 1:
        return (nums1[0] + nums2[0])/2
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

    # 第一个列表的中位数
    m1 = nums1[len1/2]
    # 第二个列表的中位数
    m2 = nums1[len2/2]

    if m1 >= m2:
        # 可以改成三元表达式
        # 奇数取前面len/2,去后面len/2+1,偶数不动都是len/2
        nums1 = nums1[0:len1/2]
        if len2%2 == 1:
            nums2 = nums2[len2/2+1:]
        else:
            nums2 = nums2[len2/2:]
    else:
        if len1%2 == 1:
            nums1 = nums1[len1/2+1:]
        else:
            nums1 = nums1[len1/2:]
        nums2 = nums2[0:len2/2]
    return findMedianSortedArrays(nums1,nums2)




if __name__ == '__main__':
    print("hello world")
