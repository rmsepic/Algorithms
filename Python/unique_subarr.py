def sliding(arr, n):
    pass

# This solution does not work for when the whole array counts
# Does not count subarrays by moving the left index
def unique_sub(arr, n):
    sub_arr = []
    left = 0 
    right = 1
    sub_arr.append(arr[left])
    unique = 1
    unique_subs = 0

    # Initialize sub array 
    # Find what right we need 
    while unique < n:
        if arr[right] not in sub_arr:
            unique = unique + 1

        sub_arr.append(arr[right])
        right = right + 1

    # Sub arr is the first sub_arr in arr
    unique_subs = unique_subs + 1
    print("First sub", sub_arr)

    # Go again to the right and see if the new character is unique
    while right < len(arr):
        # If find a new character
        if arr[right] not in sub_arr:
            # There are already too many unique characters
            if unique == n:
                temp = sub_arr[0]

                # Reset the sliding window
                # Move left over and then set right to just in front
                left = left + 1
                right = left + 1

                # If a unique character is removed then decrement unique
                #if temp not in arr[left:right]:
                unique = 1
                if n == 1:
                    unique_subs = unique_subs + 1
                # If a unique char is not removed then there is still the same 
                # number of unique chars but it is a different sub array
                #else:
                #    unique_subs = unique_subs + 1
            # Still looking for enough unique characters
            else:
                sub_arr.append(arr[right])
                unique = unique + 1
                
                if unique == n:
                    unique_subs = unique_subs + 1

                right = right + 1
        # Character is already in sub array
        else:
            unique_subs = unique_subs + 1
            right = right + 1

        sub_arr = arr[left:right]
        print(sub_arr, "and uni is ", unique_subs)

    return unique_subs
            

def unique_sub_naive(arr, n):
    max_ = len(arr)
    ans = 0

    for i in range(0, max_):
        unique = 0
        temp = []

        for j in range(i, max_):
            if arr[j] not in temp:
                temp.append(arr[j])
                unique += 1

                # Has the max num of unique characters
                if unique == n:
                    ans += 1
            # arr[j] is already in the list
            else:
                if unique == n:
                    ans += 1

    return ans

if __name__ == "__main__":
    #arr = [2,1,1,1,2]
    #n = 1
    
    arr = [2,1,2,1,2]
    n = 2

    ans = unique_sub(arr, n)

    print(ans)