employees = [
    ("Ramesh", 45000),
    ("Anitha", 62000),
    ("Karthik", 38000),
    ("Deepa", 75000),
    ("Sanjay", 52000),
    ("Pavan", 48000),
    ("Neha", 68000),
    ("Rohit", 41000),
    ("Swathi", 58000),
    ("Ajay", 83000)
]

stack = [(0, len(employees) - 1)]

while stack:
    low, high = stack.pop()

    if low < high:
        pivot = employees[high][1]
        i = low - 1

        for j in range(low, high):
            if employees[j][1] >= pivot:
                i += 1
                employees[i], employees[j] = employees[j], employees[i]

        employees[i + 1], employees[high] = employees[high], employees[i + 1]

        pivot_position = i + 1

        stack.append((low, pivot_position - 1))
        stack.append((pivot_position + 1, high))

print("Employees sorted by salary in descending order:")
print()

for name, salary in employees:
    print(name, "-", salary)

print()
print("Employees eligible for the salary benefit:")
print()

for name, salary in employees:
    if salary >= 50000:
        print(name, "-", salary)