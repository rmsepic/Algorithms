# This solution is an improvement from those in unique_subarr.py
# The map allows for faster checks of repeat characters

def unique(arr, n):
    ans = 0 

    right = 0

    left = 0 
    unique = 1

    left_k_min = 0
    unique_k_min = 1

    map_ = {}
    map_k_min = {}

    while right < len(arr):  
        # Found a unique character
        if arr[right] in map_:
            map_[arr[right]] += 1
        else:
            map_[arr[right]] = 1
        
        if arr[right] in map_k_min:
            map_k_min[arr[right]] += 1
        else: 
            map_k_min[arr[right]] = 1

        while len(map_) > n:
            map_[arr[left]] -= 1
            if map_[arr[left]] == 0:
                map_.pop(arr[left])

            left += 1
        
        print(map_k_min)
        while len(map_k_min) >= n:
            map_k_min[arr[left_k_min]] -= 1
            if map_k_min[arr[left_k_min]] == 0:
                map_k_min.pop(arr[left_k_min])

            left_k_min += 1

        right += 1       
        ans += left_k_min - left

    return ans


if __name__ == "__main__":

    arr = [1,2,1,2,3]
    n = 2
    # ans = 7

    ans = unique(arr, n)

    print("ans", ans)