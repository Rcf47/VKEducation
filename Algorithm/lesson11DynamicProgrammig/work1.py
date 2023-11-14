def max_product_subsequence(arr, k):
    arr.sort()
    max_product = 1
    for i in range(k):
        max_product *= arr[-i - 1]
    return max_product


input_data = input().split()
n = int(input_data[0])
k = int(input_data[1])
arr = [int(x) for x in input_data[2:]]
result = max_product_subsequence(arr, k)
print(result)
