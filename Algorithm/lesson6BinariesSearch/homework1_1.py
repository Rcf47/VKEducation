def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Get the input array of prices from the user
prices_str = input()
prices = list(map(int, prices_str))

# Get the target price from the user
target_price = 999

result = binary_search(prices, target_price)
print(result)
