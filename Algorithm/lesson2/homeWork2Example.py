n = int(input())  # число элементов в массиве
grades = list(map(int, input().split()))  # оценки

# Переносим все оценки, равные нулю, в конец массива
grades.sort(key=lambda x: x == 0)

print(*grades)
