# Returns the arrays of the distance between the indexes per row
def calcArr(rows: int) -> list:
    arr = [-1 for _ in range(rows)]
    index = rows * 2 - 3 

    for r in range(0, (rows + 1) // 2 ):
        arr[r] = index 
        arr[rows - r - 1] = index  
        index -= 2

    return arr

def convert(s: str, rows: int):
    ans = ""
    r = 0
    arr = calcArr(rows)
    print(arr)

    for a in arr:
        for x in range(r, len(s), a + 1):
            ans += s[x]

        r += 1

    return ans


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    ans = "PAHNAPLSIIGYIR"
    rows = 3

    print(convert(s, rows))
    print(convert(s, rows) == ans)
