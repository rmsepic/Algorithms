def calc(n, arr):
    for i in arr:
        if i % n != 0:
            return False

    return True

def gcd(arr):
    max_ = len(arr)
    gcd = 1
    t_gcd = 2

    for i in range(2, arr[0] + 1):
        if calc(t_gcd, arr) == True:
            gcd = t_gcd

        t_gcd = t_gcd + 1

    return gcd

if __name__ == "__main__":
    arr = [4, 4, 12]

    ans = gcd(arr)

    print(ans)