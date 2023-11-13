def exponential_search(arr, needle):
    n = len(arr)
    if arr[0] == needle:
        return [0, 0]

    left = 1
    right = 1
    while right < n and arr[right] <= needle:
        left = right
        right *= 2

    return binary_search(arr, needle, left, min(right, n - 1))


def binary_search(arr, needle, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == needle:
            return [left, right]
        elif arr[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    return [-1, -1]


n = input()
arr = list(map(int, input().split()))
needle = int(input())
result = exponential_search(arr, needle)
print(result)
