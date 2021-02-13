from shortest_path_binary_matrix import shortestPathBinaryMatrix

if __name__ == "__main__":
    nums1 = "cacc"
    nums2 = "aacc"
    s = Solution()
    n = s.isAnagram(s=nums1, t=nums2)
    print("answer: ", n)