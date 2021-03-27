def romanToInt(s: str) -> int:
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    point = 1

    for i in range(len(s) - 1, -1, -1):
        x = dic[s[i]]
        
        if x >= point:
            ans += x
            point = dic[s[i]]
        else:
            ans -= x

    return ans

if __name__ == "__main__":
    ans = romanToInt("III")
    print(ans)