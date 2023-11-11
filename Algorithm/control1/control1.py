def move_even_numbers(arr):
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers + odd_numbers


input_str = ""
if __name__ == "__main__":
    input_str = input()
arr = list(map(int, input_str.split()))
result = move_even_numbers(arr)
result_str = " ".join(map(str, result))
print(result_str)
