def count_elements(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] != element:
            count += 1
        else:
            arr[i] = None
    return count


n = int(input())
arr = list(map(int, input().split()))
element = int(input())

result = count_elements(arr, element)
print(result)
