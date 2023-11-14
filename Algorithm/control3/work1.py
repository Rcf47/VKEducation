def find_max_element(tree):
    return max(tree)


n = input()
tree = list(map(int, input().split()))
max_element = find_max_element(tree)
print(max_element)
