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


input_string = input()
price_string = input_string.split(":")[1].strip()
price_values = [int(price.strip()) for price in price_string.split(",")]

target_price_str = input()
target_price = int(target_price_str.split(":")[1].strip())

result = binary_search(price_values, target_price)
print(result)
