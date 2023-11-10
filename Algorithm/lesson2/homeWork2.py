n = int(input())
grades = list(map(int, input().split()))

grades.sort(key=lambda x: x == 0)

print(*grades)
