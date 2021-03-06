from typing import List

def largest_area(arr: List[int]) -> int:
    left = 0
    right = 1
    volume = min(arr[left], arr[right]) * (right - left)

    i = 1
    while i < len(arr) - left - 1 and right < len(arr) - 1:
        right += 1

        old_left = min(arr[left], arr[right]) * (right - left)
        new_left = min(arr[left + i], arr[right]) * (right - (left + i))
        
        print("left", arr[left], " ", arr[right])
        print("new ", arr[left + i], " ", arr[right])

        if new_left >= old_left and arr[left] < arr[left + i]:
            left = left + i
            i = 0
        
        volume = max(old_left, new_left, volume)
        print("vol ", volume)
        print("")
        i += 1

    return volume