def find_min_element(tree):
    return min(tree)


n = input()
tree = list(map(int, input().split()))
min_element = find_min_element(tree)
print(min_element)
