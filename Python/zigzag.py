def convert(s: str, rows: int):
    ans = ""

    idx = 0
    x = 1
    
    while len(ans) < len(s):
        print(idx)
        ans += s[idx]
        idx += rows + 1
        if idx >= len(s):
            idx = x 
            x += 1


    return ans


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    rows = 3

    print(convert(s, rows))
