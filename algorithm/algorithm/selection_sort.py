def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 마지막 요소는 자동으로 정렬되므로 n-1까지 반복
        min_index = i  # 현재 위치를 최소값의 인덱스로 설정
        for j in range(i + 1, n):  # i 이후의 요소들을 탐색
            if arr[j] < arr[min_index]:  # 더 작은 값을 찾으면
                min_index = j  # 최소값 인덱스 갱신
        # 현재 위치와 최솟값 위치를 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
