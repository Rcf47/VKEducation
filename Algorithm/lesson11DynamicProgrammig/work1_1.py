def max_product_subsequence(arr, k):
    arr.sort()
    max_product = 1
    for i in range(k):
        max_product *= arr[-i - 1]
    return max_product


n = int(input())
k = int(input())
input_data = input().split()
arr = input_data
result = max_product_subsequence(arr, k)
print(result)
