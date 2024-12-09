def sequential_search(arr, key, low, high):
    for i in range(low, high+1):
        if arr[i] == key :
            return i
    return -1