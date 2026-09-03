profits = [10, -5, 20, -10, 30, -15, 5, -2, 8, -20]

current_sum = profits[0]
maximum_sum = profits[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(profits)):
    if profits[i] > current_sum + profits[i]:
        current_sum = profits[i]
        temp_start = i
    else:
        current_sum = current_sum + profits[i]

    if current_sum > maximum_sum:
        maximum_sum = current_sum
        start = temp_start
        end = i

print("Daily Profit/Loss:")
print(profits)

print()
print("Maximum Profit:")
print(maximum_sum)

print()
print("Days included:")
for i in range(start, end + 1):
    print("Day", i + 1, ":", profits[i])