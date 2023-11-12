def is_anagram(a, b):
    if len(a) != len(b):
        return False

    count = {}

    for char in a:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in b:
        if char in count:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        else:
            return False

    return len(count) == 0


input_str = input()
a, b = input_str.split(", ")
print(is_anagram(a, b))
