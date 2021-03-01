def detected(num, sub_arr):
    pass

def unique_sub(arr, n):
    max_ = len(arr)

    for left in range(0, max_):

def unique_sub_naive(arr, n):
    max_ = len(arr)
    ans = 0

    for i in range(0, max_):
        unique = 0
        temp = []

        for j in range(i, max_):
            print("is ",  arr[j], "in ", temp)
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
    n = 2
    arr = [1,2,3,1,2]
    max_cache_size = 2

    ans = unique_sub(arr, n)

    print(ans)