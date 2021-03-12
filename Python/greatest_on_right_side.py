from typing import List

def greatestOnRightSide(arr: list):
    # Go from right to left
    greatest = arr[len(arr) - 1]
    arr[len(arr) - 1] = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < greatest:
            arr[i] = greatest
        # arr[i] is greater than
        else:
            #temp = greatest
            #greatest = arr[i]
            #arr[i] = temp   
            greatest, arr[i] = arr[i], greatest        

    return arr

if __name__ == "__main__":
    #arr = [16, 17, 4, 3, 5, 2]
    arr = [2,3,1,9]

    ans = greatestOnRightSide(arr)
    print(ans)