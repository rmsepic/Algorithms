from typing import List

def largest_area(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    f_vol = lambda x, y, arr: min(arr[x], arr[y]) * (y - x)
    left_ans = left
    right_ans = right
    vol = f_vol(left, right, arr)

    while left < right:
        # Is the left pointer shorter than the right
        if arr[left] <= arr[right]:
            left += 1
        # Right pointer is smaller than the left
        else:
            right += 1
            
        if f_vol(left, right, arr) > vol:
            vol = f_vol(left, right, arr)

    return vol

if __name__ == "__main__":
    arr = [2,3,10,5,7,8,9]
    ans = largest_area(arr)
    print(ans)