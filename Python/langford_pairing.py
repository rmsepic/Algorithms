# Recurssive and iterative solutions for generating a 
# Langford paired array 
# Only works for numbers that have Langford pairs
# Does not work for N = 5, N = 6

from typing import List

def lang(N: int, arr: List, index: int, ht: dict):
    if N == 0:
        return arr
    
    # Place the next one
    if index + N + 1 < len(arr) and arr[index] == -1 and arr[index + N + 1] == -1:
        arr[index] = N 
        arr[index + N + 1] = N
        ht[N] = index
        ans = lang(N - 1, arr, 0, ht)
    # Try the next location
    elif index + N + 1 < len(arr) and (arr[index] > 0 or arr[index + N + 1] > 0):
        lang(N, arr, index + 1, ht)
    # Roll it back
    else:
        index = ht[N + 1]
        arr[index] = -1
        arr[index + N + 1 + 1] = -1
        ht.pop(N + 1)
        lang(N + 1, arr, index + 1, ht)

    return arr


def langford(N: int):
    arr = [-1 for i in range(0, 2 * N)]
    ht = {}
    arr[0] = N 
    arr[N + 1] = N
    index = 1
    ht[N] = 0
    
    ans = lang(N - 1, arr, index, ht)

    return ans

# _,_,_,_,_,_,_,_,_,_
# 6,4,5,_,_,_,4,6,5,_,_,_

def helper(N: int, arr: List, start: int, ht: dict):
    for index in range(start, len(arr) - N - 1):
        # If the path is clear
        if arr[index] == -1 and arr[index + N + 1] == -1:
            arr[index] = N 
            arr[index + N + 1] = N
            ht[N] = index
            return True 

    return False

def langford_loop(N: int):
    arr = [-1 for i in range(0, 2 * N)]
    ht = {}
    #index = 0
    start = 0

    # Loop through numbers and place them
    while N > 0:
        print(arr, N)
           
        if helper(N, arr, start, ht) == True:
            N -= 1
            start = 0
        # Could not place N
        # Have to go to N + 1 and place it somewhere else
        else:
            N += 1 
            arr[ht[N]] = -1
            arr[ht[N] + N + 1] = -1
            start = ht[N] + 1
            ht.pop(N)
           

    return arr

    
# Checks if the array is a valid Langford Pair    
def check(arr: List) -> bool:
    for i in range(0, len(arr) // 2):
        n = arr[i]
        print(arr[i], arr[n + i + 1], arr[i - n - 1])
        if arr[i] != arr[n + i + 1] and arr[i] != arr[i - n - 1]:
            return False 

    return True



if __name__ == "__main__":
    N = 8
    ans = langford_loop(N)
    print(ans)
    print(check(ans))
    ans_loop = langford_loop(N)
    print(ans, ans_loop)

    print(ans == ans_loop)

    print(check(ans_loop))