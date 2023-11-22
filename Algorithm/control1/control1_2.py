def move_even_numbers_to_start(arr):
    next_even = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[next_even] = arr[next_even], arr[i]
            next_even += 1
    return arr


arr = list(map(int, input().split()))
result = move_even_numbers_to_start(arr)
print(" ".join(str(num) for num in result))
