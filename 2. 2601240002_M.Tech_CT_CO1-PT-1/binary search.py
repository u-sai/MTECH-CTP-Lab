books = list(range(1, 1000001))

book_no = int(input("Enter the book number to search: "))

low = 0
high = len(books) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if books[mid] == book_no:
        found = True
        position = mid + 1
        break
    elif books[mid] < book_no:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Book found")
    print("Book Number:", book_no)
    print("Book Position:", position)
else:
    print("Book not found")