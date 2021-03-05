import threading

class Window:
    def __init__(self):
        self.result = 0

    def sliding(self, arr, n):
        left = 0
        right = 1

        sub_arr = arr[left:right]
        unique = 1
        unique_subs = 1

        while right < len(arr):
            new_char = arr[right]
            
            if new_char not in sub_arr:
                unique += 1

            # Too many unique characters
            while unique > n:
                sub_arr = arr[left + 1: right]

                # Removed a unique character
                if arr[left] not in sub_arr:
                    unique -= 1

                left += 1

            unique_subs += right - left + 1
            right += 1
            sub_arr = arr[left:right]

        self.result = unique_subs

def unique(arr, n):
    w1 = Window()
    w2 = Window()
    t1 = threading.Thread(group=None, target=w1.sliding, name="Thread 1", args=(arr, n))
    t1.start()

    print(w1.result)
    if n == 1:
        return w1.result

    t2 = threading.Thread(group=None, target=w2.sliding, name="Thread 2", args=(arr, n - 1))
    t2.start()

    t1.join()
    t2.join()

    return w1.result - w2.result

if __name__ == "__main__":
    arr = [1,2,1,2,3]
    n = 2
    # ans 10

    ans = unique(arr, n)
    print(ans)

