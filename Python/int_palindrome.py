# 10:53

import math

# Attempted solution only using math operations
def getLower(n: int, order: int, i: int) -> int:
    print("\n\n\n")
    ans = n
    while order > i:
        print("new: ", n // (10 ** (order)))
        temp = ans // (10 ** (order))
        print("temp order", temp)
        temp *= 10 ** (order)
        print("temp: ", temp)
        ans -= temp
        print("ans", ans)
        order -= 1

    ans = ans // (10 ** i)

    print("get low", ans)
    return ans


def isPalindrome(x: int) -> bool:
    # Cannot have a palindromic negative number
    if x < 0:
        return False

    max_order = math.floor(math.log(x, 10))

    i = 0
    low = getLower(x, max_order, i)
    high = x // (10 ** (max_order - i))
    #print((high * (10**(max_order - i))))
    x = x - (high * (10**(max_order - i))) - (low ** (10 ** i))
    print("nums", x, low, high)
    while low <= high:
        if high != low:
            return False 

        i += 1
        low = getLower(x, max_order, i)
        high = x // (10 ** (max_order - i))
        print("arith: ", (10**(max_order - i)), (low ** (10 ** i)))
        x = x - (high * (10**(max_order - i))) - (low ** (10 ** i))
        print("nums", x, low, high)

        

    return True

# Correct working answer
def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_str = str(x)
        
        i = 0
        j = len(x_str) - 1
        while i <= j:
            if x_str[i] == x_str[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
            
        return True


if __name__ == "__main__":
    x = 1221
    ans = isPalindrome(x)
    print(ans)