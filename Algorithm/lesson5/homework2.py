def remove_duplicates(s):
    result = []
    for char in s:
        if len(result) > 0 and result[-1] == char:
            result.pop()
        else:
            result.append(char)
    return "".join(result)


s = input()
result = remove_duplicates(s)
print(result)
