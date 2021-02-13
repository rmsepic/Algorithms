import math

from typing import List


def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
    A = nums1
    B = nums2
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            print("Here")
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # CONSTRAINTS
    # 1 <= m + n <= 2000
    # where |nums1| = m and |nums2| = n
    if len(nums1) == 0:
        if (len(nums2) % 2 == 0):
            x = len(nums2) // 2 - 1
            y = len(nums2) // 2
            return (nums2[x] + nums2[y]) / 2
        else: 
            x = len(nums2) // 2
            return nums2[x]
    elif len(nums2) == 0:
        if (len(nums1) % 2 == 0):
            i = len(nums1) // 2 - 1
            j = len(nums1) // 2
            return (nums1[i] + nums1[j]) / 2
        else: 
            i = len(nums1) // 2
            return nums1[i]

    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp

    m = len(nums1)
    n = len(nums2)
    left = 0
    right = m

    while left <= right:
        i = (left + right) // 2
        j = ((n + m + 1) // 2) - i
        print("i ", i)
        print("j ", j)
        print(nums1[i-1])
        #print(nums2[j])
        if i < m and nums1[i] < nums2[j-1]:
            left = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            right = i - 1
        else:
            if i == 0:
                left_max = nums2[j-1]
            elif j == 0:
                left_max = nums1[i-1]
            else:
                left_max = max(nums1[i-1], nums2[j - 1])


            print("left max ", left_max)
            # If even
            if (m + n) % 2 == 0:
                print("it's even")
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    print("here")
                    right_min = min(nums1[i], nums2[j])

                print("left m ", left_max)
                print("right m ", right_min)
                return (left_max + right_min) / 2
            else:
                return left_max


        