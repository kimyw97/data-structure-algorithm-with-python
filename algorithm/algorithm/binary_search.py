def binary_search(arr, key, low, high):
    if(low <= high) :
        middle = (low + high) // 2 # 중앙값 찾기
        if key == arr[middle]: # 중앙값이랑 비교값이랑 같은지 확인
            return middle
        elif key < arr[middle]: # 비교값이 더 작으면 왼쪽 확인
            return binary_search(arr, key, low, middle -1)
        else: # 그외는 오른쪽 확인
            return binary_search(arr, key , middle + 1, high)
    return -1

def binary_search_iter(arr, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == arr[middle]:
            return middle
        elif key > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return -1