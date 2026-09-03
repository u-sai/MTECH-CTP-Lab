points = [
    ("ATM1", 2, 3),
    ("ATM2", 8, 7),
    ("ATM3", 4, 6),
    ("ATM4", 12, 10),
    ("ATM5", 5, 5),
    ("ATM6", 9, 8),
    ("ATM7", 15, 14),
    ("ATM8", 3, 4),
    ("ATM9", 11, 9),
    ("ATM10", 20, 18)
]

import math

minimum_distance = float("inf")
closest_atm1 = ""
closest_atm2 = ""

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1 = points[i][1]
        y1 = points[i][2]

        x2 = points[j][1]
        y2 = points[j][2]

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance < minimum_distance:
            minimum_distance = distance
            closest_atm1 = points[i][0]
            closest_atm2 = points[j][0]

print("ATM Locations:")
print()

for name, x, y in points:
    print(name, ":", "(", x, ",", y, ")")

print()
print("Closest pair of ATMs:")
print(closest_atm1, "and", closest_atm2)
print("Distance:", round(minimum_distance, 2))