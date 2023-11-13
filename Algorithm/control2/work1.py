def find_majority_element(arr):
    n = len(arr)
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1


# Пример использования
n = int(input())
arr = list(map(int, input().split()))

result = find_majority_element(arr)
print(result)
