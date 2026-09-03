students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Arun", 78),
    ("Sneha", 95),
    ("Kiran", 88),
    ("Divya", 91),
    ("Ravi", 67),
    ("Anjali", 89),
    ("Vijay", 96),
    ("Pooja", 93)
]

n = len(students)

size = 1

while size < n:
    left = 0

    while left < n:
        mid = min(left + size, n)
        right = min(left + 2 * size, n)

        i = left
        j = mid
        temp = []

        while i < mid and j < right:
            if students[i][1] >= students[j][1]:
                temp.append(students[i])
                i += 1
            else:
                temp.append(students[j])
                j += 1

        while i < mid:
            temp.append(students[i])
            i += 1

        while j < right:
            temp.append(students[j])
            j += 1

        for k in range(len(temp)):
            students[left + k] = temp[k]

        left += 2 * size

    size *= 2

print("Students sorted in descending order:")
print()

for name, marks in students:
    print(name, "-", marks)

print()
print("Students eligible for scholarship:")
print()

for name, marks in students:
    if marks >= 90:
        print(name, "-", marks)