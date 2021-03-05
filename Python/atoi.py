def atoi(string: str) -> int:
    ans = x = 0
    flag = True
    neg = False

    # Remove whitespace at beginning and ending of string
    s = string.strip()

    if len(string) == 0:
        return 0

    # Check if positive or negative
    if s[0] == '-':
        neg = True
        x = 1

    if s[0] == '+':
        x = 1

    for i in range(x, len(s)):
        if s[i].isdigit() and flag == True:
            ans += (10 ** (len(s) - i - 1)) * int(s[i])
        else:
            flag = False
            ans //= 10

    if neg == True:
        ans *= -1

    if ans > (2 ** 31) - 1:
        ans = (2 ** 31) - 1
    elif ans < (2 ** 31) * -1:
        ans = (2 ** 31) * -1

    return ans