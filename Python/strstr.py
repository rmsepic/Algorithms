def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
            return 0
    
    for i in range(0, len(haystack) - len(needle) + 1):
        if needle == haystack[i:len(needle)+i]:
            return i
        
    return -1


if __name__ == "__main__":
    needle = "c"
    haystack = "abc"
    ans = strStr(haystack, needle)
    print(ans)