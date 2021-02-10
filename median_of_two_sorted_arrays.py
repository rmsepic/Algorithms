import math

from typing import List

class Solution:
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

        size = len(nums1) + len(nums2)
        arr1 = nums1
        arr2 = nums2
        i = len(nums1) // 2 
        x = len(nums2) // 2

        while len(arr1) > 2 or len(arr2) > 2:
            if arr1[i] > arr2[x]:
                if len(arr1) > 2:
                    arr1 = arr1[:i+1]

                if len(arr2) > 2:
                    arr2 = arr2[x:]
            elif arr1[i] < arr2[x]:
                if len(arr1) > 2:
                    arr1 = arr1[i:]

                if len(arr2) > 2:
                    arr2 = arr2[:x+1]
            # If they are equal then that is the median
            else:
                if len(arr1) % 2 == 0 and len(arr2) % 2 == 0:
                    if len(arr1) > 2:
                        arr1 = arr1[:i]

                    if len(arr2) > 2:
                        arr2 = arr2[x:]
                else:
                    return arr1[i]


            print(arr1)
            print(arr2)
            i = len(arr1) // 2 
            x = len(arr2) // 2


        i = len(arr1) // 2 - 1
        j = len(arr1) // 2 
        x = len(arr2) // 2 - 1
        y = len(arr2) // 2 

        # IF even
        if len(arr1) % 2 == 0:
            # IF even
            if len(arr2) % 2 == 0:
                if arr1[i] < arr2[x] and arr1[j] < arr2[y]:
                    return (arr1[j] + arr2[x]) / 2
                elif arr1[i] > arr2[x] and arr1[j] > arr2[y]:
                    return (arr1[j] + arr2[x]) / 2
                elif arr1[i] <= arr2[x] and arr1[j] >= arr2[y]:
                    return (arr2[x] + arr2[y]) / 2
                elif arr1[i] >= arr2[x] and arr1[j] <= arr2[y]:
                    return (arr1[i] + arr1[j]) / 2
            else:
                if size % 2 == 0 and size > 2:    
                    if arr1[i] < arr2[x] and arr1[j] > arr2[x]:
                        return (arr1[i] + arr2[x]) / 2
                    else:
                        return (arr1[i] + arr1[j]) / 2

                if arr2[x] >= arr1[j]:
                    return arr1[j]
                elif arr2[x] < arr1[j] and arr2[x] > arr1[i]:
                    return arr2[x]
                else:
                    return arr1[i]
        # If odd
        else:
            if size % 2 == 0 and size > 2:
                if arr1[i] >= arr2[y]:
                    return (arr2[x] + arr2[y]) / 2
                elif arr1[i] > arr2[x] and arr1[i] < arr2[y]:
                    return (arr1[i] + arr2[x]) / 2
                else:
                    return  (arr2[x] + arr2[y]) / 2

            if len(arr2) % 2 == 0:
                if arr1[i] >= arr2[y]:
                    return arr2[y]
                elif arr1[i] > arr2[x] and arr1[i] < arr2[y]:
                    return arr1[i]
                else:
                    return arr2[x]
            else:
                return (arr1[i] + arr2[x]) / 2

if __name__ == "__main__":
    nums1 = [2]
    nums2 = [1,3,5]
    s = Solution()
    n = s.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print("answer: ", n)

            