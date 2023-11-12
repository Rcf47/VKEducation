def find_last_even(arr):
    stack = []
    for num in arr:
        if num % 2 == 0:
            stack.append(num)
    if len(stack) > 0:
        return stack[-1]
    else:
        return -1


n = int(input())
arr = list(map(int, input().split()[:n]))

result = find_last_even(arr)
print(result)
