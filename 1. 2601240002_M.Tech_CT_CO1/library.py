def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


n = int(input("Enter the number of books: "))

accession_numbers = []

for i in range(n):
    number = int(input(f"Enter accession number {i + 1}: "))
    accession_numbers.append(number)

sorted_numbers = merge_sort(accession_numbers)

print("\nAccession numbers in ascending order:")
print(sorted_numbers)