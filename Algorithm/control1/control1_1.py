def move_even_numbers(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    return even_numbers + odd_numbers


input_data = input()
arr = list(map(int, input_data.split()))
new_arr = move_even_numbers(arr)
print(" ".join(map(str, new_arr)))
