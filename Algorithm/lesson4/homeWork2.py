n = int(input())
books = []

for _ in range(n):
    line = input()
    first_quote = line.index('"')
    last_quote = line.rindex('"')
    isbn = line[:first_quote].strip()
    title = line[first_quote + 1 : last_quote]
    year = int(line[last_quote + 1 :].strip())
    books.append((isbn, title, year))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] < right[j][2]:
            merged.append(left[i])
            i += 1
        elif left[i][2] > right[j][2]:
            merged.append(right[j])
            j += 1
        else:
            if left[i][1] < right[j][1]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


sorted_books = merge_sort(books)

for book in sorted_books:
    print(f'{book[0]} "{book[1]}" {book[2]}')
