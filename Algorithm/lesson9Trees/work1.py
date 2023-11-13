def find_min_max_product(arr):
    if length == 0:
        return None

    min_value = arr[0]
    max_value = arr[0]

    for i in range(1, length):
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]

    return min_value * max_value


length = int(input())
arr = list(map(int, input().split()))
result = find_min_max_product(arr)
print(result)
