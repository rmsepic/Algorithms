from typing import List

def lang(N: int, arr: List, index: int):
    print(arr)
    if index + N + 1 > len(arr):
        if arr.count(-1) > 0:
            index = arr.index(-1)
        else:
            return -1

    # The array has place for this
    if arr[index] == -1 and arr[index + N + 1] == -1:
        arr[index] = N 
        arr[index + N + 1] = N
        index += 1
        return lang(N - 1, arr, index)
    # The array has reached a contradiction
    else:
        return lang(N, arr, index + 1)


def langford(N: int):
    arr = [-1 for i in range(0, 2 * N)]
    
    arr[0] = N 
    arr[N + 1] = N
    index = 1

    return lang(N - 1, arr, index)

# _,_,_,_,_,_,_,_,_,_
# 5,_,4,_,_,_,5,4,_,_

def langford_loop(N: int):
    ht = {} # Hold the number and its index
    arr = [-1 for i in range(0, 2 * N)]
    start = 1
    i = 0

    while N > 0:
        # Add the new number
        if i + N + 1 < len(arr) and arr[i] == -1 and arr[i + N + 1] == -1:
            arr[i] = N 
            arr[i + N + 1] = N
            ht[N] = i
            N -= 1
        # Can't fit that number
        elif i >= len(arr):
            arr[ht[N + 1]] = -1
            arr[ht[N + 1] + N + 2] = -1
            print("removed: ", arr)
            ht.pop(N + 1)
            i = start 
            start = ht[N + 1] + 1
            N += 1
        
        print(i)
        print(ht)
        print(arr)
        i += 1
        

    return arr

    
# Checks if the array is a valid Langford Pair    
def check(arr: List) -> bool:
    for i in range(0, len(arr) // 2):
        n = arr[i]
        if arr[i] != arr[n + i]:
            return False 

    return True



if __name__ == "__main__":
    N = 4
    ans = -1 #langford(N)
    ans_loop = langford_loop(N)
    print(ans, ans_loop)

    print(ans == ans_loop)

    print(check(ans_loop))