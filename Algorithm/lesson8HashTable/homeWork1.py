def max_repeated_letters(string):
    letter_count = {}
    max_count = 0

    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

        if letter_count[letter] > max_count:
            max_count = letter_count[letter]

    return max_count


string = input()
max_count = max_repeated_letters(string)
print(max_count)
