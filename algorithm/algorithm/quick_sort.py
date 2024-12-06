def quick_sort(arr):
    if len(arr) <= 1:  # 배열의 길이가 1 이하이면 정렬 완료
        return arr
    pivot = arr[len(arr) // 2]  # 피벗 선택, 어떤걸 선택하든 상관 없음
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 값
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 값
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값
    return quick_sort(left) + middle + quick_sort(right)