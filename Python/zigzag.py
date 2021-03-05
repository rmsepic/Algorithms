def convert(s: str, rows: int):
    ans = ""
    rows_ = rows
    x = rows_ * 2 - 3 + 1

    for r in range(0, rows):
        for a in range(r, len(s), x):
            ans += s[a]

        rows_ -= 1
        x = rows_ * 2 - 3 + 1
        print(r, x)
        if r == 1:
            x = rows * 2 - 3 + 1

    return ans


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    rows = 3

    print(convert(s, rows))
