# Returns the arrays of the distance between the indexes per row
def calcArr(rows: int) -> list:
    arr = [(1, 1) for _ in range(rows)]
    left = rows * 2 - 3 
    right = 1

    arr[0] = (left, left)
    arr[rows - 1] = (left, left)

    left -= 2

    for r in range(1, (rows + 1) // 2 ):
        arr[r] = (left, right)
        arr[rows - r - 1] = (right, left)  
        left -= 2
        right += 2
        
    return arr

def convert(s: str, rows: int):
    if rows == 1:
        return s

    ans = ""
    r = x = 0
    arr = calcArr(rows)
    print(arr)
    for a in arr:
        x = r
        b = 0
        while x < len(s):
            ans += s[x]
            x += a[b] + 1
            b = 1 - b

        r += 1

    return ans


