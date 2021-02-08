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

        tot_size = len(nums1) + len(nums2)

        # Start with nums1
        # If even
        if (len(nums1) % 2) == 0:
            i = len(nums1) // 2 - 1
            j = len(nums1) // 2

            # If BOTH are even
            if (len(nums2) % 2 == 0):
                x = len(nums1) // 2 - 1
                y = len(nums1) // 2

                if nums1[i] <= nums2[x] and nums1[j] <= nums2[y]:
                    return (nums1[j] + nums2[x]) / 2
                elif nums1[i] <= nums2[x] and nums1[j] >= nums2[y]:
                    return (nums2[x] + nums2[y]) / 2
                elif nums1[i] >= nums2[x] and nums1[j] <= nums2[y]:
                    return (nums1[i] + nums1[j]) / 2
                elif nums1[i] >= nums2[x] and nums1[j] >= nums2[y]:
                    return (nums1[i] + nums2[y]) / 2
            else:
                x = len(nums2) // 2

                if nums1[i] >= nums2[x]:
                    return nums1[i]
                elif nums1[i] < nums2[x] and nums2[x] < nums1[j]:
                    return nums2[x]
                elif nums2[x] >= nums1[j]:
                    return nums1[j]
        # If odd
        else:
            i = len(nums1) // 2

            if (len(nums2) % 2 == 0):
                x = len(nums2) // 2 - 1
                y = len(nums2) // 2

                if nums1[i] <= nums2[x]:
                    return nums2[x]
                elif nums1[i] < nums2[y] and nums2[x] < nums1[i]:
                    return nums1[i]
                elif nums2[y] <= nums1[i]:
                    print(nums2[x])
                    return nums2[y]
            # If BOTH are odd
            else:
                x = len(nums2) // 2
                return (nums1[i] + nums2[x]) / 2

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [4,5,6]
    s = Solution()
    n = s.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print("answer: ", n)

            