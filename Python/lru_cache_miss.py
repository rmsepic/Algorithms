def lruCacheMiss(num_requests, page_list, max_size):
    if max_size == 0 or num_requests == 0 or len(page_list) == 0:
        return 0

    cache = []
    misses = 0

    for page in page_list:
        if page in cache:
            # Cache hit
            cache.pop(cache.index(page))
            cache.append(page)
        else:
            misses += 1
            # Cache miss
            if len(cache) < max_size:
                cache.append(page)
            else:
                cache.pop(0)
                cache.append(page)

        if len(cache) > max_size:
            print("ERROR")

        print(cache)

    return misses


if __name__ == "__main__":
    num = 10
    pages = [8, 3, 6, 2, 8, 8, 2, 6, 6, 7]
    max_cache_size = 2

    ans = lruCacheMiss(num, pages, max_cache_size)

    print(ans)