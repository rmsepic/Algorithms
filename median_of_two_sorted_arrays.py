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

        # Set ranges
        arr1 = nums1
        arr2 = nums2

        # Cut in half
        i = len(nums1) // 2
        x = len(nums2) // 2

        up_high = True
        

        while len(arr1) + len(arr2) > 2:
            if arr1[i] > arr2[x]:
                temp = arr1[i]
                arr1 = arr1[:i]
                arr2 = arr2[x:]
                if len(arr1) != 1:
                    arr1.append(temp)

                up_high = True
            elif arr1[i] < arr2[x]:
                arr1 = arr1[i:]
                temp = arr2[x]
                arr2 = arr2[:x]
                if len(arr2) != 1:
                    arr2.append(temp)

                up_high = False
            else:
                return arr1[i]
                
            i = len(arr1) // 2
            x = len(arr2) // 2

            print("Arr1: ", arr1)
            print("Arr2: ", arr2)

        if size % 2 == 0:
            return (arr1[0] + arr2[0]) / 2
        else:
            if up_high == False:
                return arr1[0]
            else:
                return arr2[0]


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [-1,3]
    s = Solution()
    n = s.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print("answer: ", n)

            