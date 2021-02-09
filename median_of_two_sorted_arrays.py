import math

from typing import List

class Solution:
    def checkSmallArrays(nums1: List[int], nums2: List[int]) -> float:
        print("check arr1: ", nums1)
        print("Check arr2: ", nums2)

        i = len(nums1) // 2 - 1
        j = len(nums1) // 2
        x = len(nums2) // 2 - 1
        y = len(nums2) // 2 

        print("I: ", i)
        print("J: ", j)
        print("X: ", x)
        print("Y: ", y)

        # If even
        if (len(nums1) % 2) == 0:
            # If BOTH are even
            if (len(nums2) % 2 == 0):
                if nums1[i] <= nums2[x] and nums1[j] <= nums2[y]:
                    return (nums1[j] + nums2[x]) / 2
                elif nums1[i] <= nums2[x] and nums1[j] >= nums2[y]:
                    return (nums2[x] + nums2[y]) / 2
                elif nums1[i] >= nums2[x] and nums1[j] <= nums2[y]:
                    return (nums1[i] + nums1[j]) / 2
                elif nums1[i] >= nums2[x] and nums1[j] >= nums2[y]:
                    return (nums1[i] + nums2[y]) / 2
            else:
                if nums1[i] >= nums2[x]:
                    return nums1[i]
                elif nums1[i] < nums2[x] and nums2[x] < nums1[j]:
                    return nums2[x]
                elif nums2[x] >= nums1[j]:
                    return nums1[j]
        # If odd
        else:
            if (len(nums2) % 2 == 0):
                if nums1[i] <= nums2[x]:
                    return nums2[x]
                elif nums1[i] < nums2[y] and nums2[x] < nums1[i]:
                    return nums1[i]
                elif nums2[y] <= nums1[i]:
                    return nums2[y]
            # If BOTH are odd
            else:
                x = len(nums2) // 2
                return (nums1[i] + nums2[x]) / 2

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

        # Set ranges
        arr1 = nums1
        arr2 = nums2

        # Cut in half
        i = len(nums1) // 2
        x = len(nums2) // 2

        while len(arr1) + len(arr2) >= 4:
            if arr1[i] >= arr2[x]:
                arr1 = arr1[:i+1]
                arr2 = arr2[x:]
            elif arr1[i] <= arr2[x]:
                arr1 = arr1[i:]
                arr2 = arr2[:x+1] 
                
            i = len(arr1) // 2
            x = len(arr2) // 2

            print("Arr1: ", arr1)
            print("Arr2: ", arr2)



        return Solution.checkSmallArrays(nums1=arr1, nums2=arr2)
        
        


if __name__ == "__main__":
    nums1 = [7]
    nums2 = [2,3,4,11]
    s = Solution()
    n = s.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print("answer: ", n)

            